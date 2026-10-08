from __future__ import annotations

from typing import Any, Dict


def run_territory_planning(state: Dict[str, Any]) -> Dict[str, Any]:
    accounts = state.get("account_data", [])
    state["territory_plan"] = {
        "territory_id": state.get("intent", {}).get("territory_id") or "T001",
        "summary": {"total_accounts": len(accounts), "revenue": sum(float(a.get("annual_revenue", 0.0)) for a in accounts), "growth": 0.13, "pipeline": 2100000},
        "priority_accounts": [a["account_id"] for a in accounts[:3]],
        "recommended_actions": [{"account": a["account_id"], "reason": "Priority account", "playbook": "Expansion Playbook"} for a in accounts[:3]],
        "strategy": {"short_term_priorities": ["Focus on expansion accounts"], "at_risk_accounts": ["ACC1040"]},
    }
    return state
