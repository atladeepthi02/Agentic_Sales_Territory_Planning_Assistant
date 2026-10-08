const metrics = [
  { label: 'Territory', value: 'T001' },
  { label: 'Total Accounts', value: '42' },
  { label: 'Revenue', value: '$8.4M' },
  { label: 'Growth', value: '12.8%' },
  { label: 'Pipeline', value: '$2.1M' },
  { label: 'At-Risk', value: '5' },
];

const accounts = [
  { name: 'ABC Retail', score: 0.91, priority: 'HIGH', reason: 'High growth + expansion opportunity' },
  { name: 'Summit Foods', score: 0.87, priority: 'HIGH', reason: 'Strong engagement and healthy pipeline' },
  { name: 'ValueMart', score: 0.62, priority: 'MEDIUM', reason: 'Service issues need follow-up' },
];

const workflow = ['Triage', 'Data Retrieval', 'KPI Analysis', 'Prioritization', 'RAG', 'Investigation', 'Planning', 'Validation', 'Response'];

export default function HomePage() {
  return (
    <main className="min-h-screen bg-slate-950 text-slate-100">
      <div className="mx-auto max-w-7xl px-6 py-8">
        <header className="mb-8 flex items-center justify-between">
          <div>
            <p className="text-sm uppercase tracking-[0.2em] text-cyan-400">Agentic Sales Assistant</p>
            <h1 className="mt-2 text-4xl font-bold">Sales Territory Planning</h1>
          </div>
          <button className="rounded-lg bg-cyan-500 px-4 py-2 font-medium text-slate-950">Analyze Territory</button>
        </header>

        <section className="mb-8 grid gap-4 md:grid-cols-6">
          {metrics.map((item) => (
            <div key={item.label} className="rounded-xl border border-slate-800 bg-slate-900 p-4 shadow-lg">
              <p className="text-xs uppercase tracking-wider text-slate-400">{item.label}</p>
              <p className="mt-2 text-2xl font-semibold">{item.value}</p>
            </div>
          ))}
        </section>

        <section className="mb-8 grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="mb-4 text-xl font-semibold">Workflow</h2>
            <div className="flex flex-wrap gap-2">
              {workflow.map((step, index) => (
                <div key={step} className="rounded-full border border-cyan-500/40 bg-cyan-500/10 px-3 py-1 text-sm text-cyan-200">
                  {index + 1}. {step}
                </div>
              ))}
            </div>
          </div>
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="mb-4 text-xl font-semibold">Approval Required</h2>
            <ul className="space-y-2 text-sm text-slate-300">
              <li>• Schedule expansion meeting for ABC Retail</li>
              <li>• Create strategic opportunity for Summit Foods</li>
              <li>• Escalate ValueMart service issue</li>
            </ul>
          </div>
        </section>

        <section className="grid gap-6 lg:grid-cols-[1.2fr_0.8fr]">
          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="mb-4 text-xl font-semibold">Priority Accounts</h2>
            <div className="space-y-4">
              {accounts.map((account) => (
                <div key={account.name} className="rounded-lg border border-slate-800 bg-slate-950 p-4">
                  <div className="flex items-center justify-between">
                    <div>
                      <h3 className="text-lg font-medium">{account.name}</h3>
                      <p className="text-sm text-slate-400">{account.reason}</p>
                    </div>
                    <div className="text-right">
                      <p className="text-sm text-slate-400">Priority</p>
                      <p className="text-lg font-bold text-cyan-400">{account.priority}</p>
                    </div>
                  </div>
                  <div className="mt-3 flex items-center gap-3">
                    <div className="h-2 flex-1 rounded-full bg-slate-800">
                      <div className="h-2 rounded-full bg-cyan-500" style={{ width: `${account.score * 100}%` }} />
                    </div>
                    <span className="text-sm font-semibold text-cyan-300">{account.score.toFixed(2)}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
            <h2 className="mb-4 text-xl font-semibold">Sources</h2>
            <ul className="space-y-3 text-sm text-slate-300">
              <li className="rounded-lg border border-slate-800 bg-slate-950 p-3">
                <p className="font-medium text-cyan-300">Expansion Playbook</p>
                <p className="mt-1 text-slate-400">Version v3 • section 2.1</p>
              </li>
              <li className="rounded-lg border border-slate-800 bg-slate-950 p-3">
                <p className="font-medium text-cyan-300">Territory Ownership Policy</p>
                <p className="mt-1 text-slate-400">Version v2 • approval requirement</p>
              </li>
            </ul>
          </div>
        </section>
      </div>
    </main>
  );
}
