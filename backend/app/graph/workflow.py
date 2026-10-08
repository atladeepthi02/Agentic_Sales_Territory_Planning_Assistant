from __future__ import annotations

from typing import Any, Dict

try:
    from langgraph.graph import END, StateGraph
except Exception:  # pragma: no cover
    END = "__END__"
    class StateGraph:  # type: ignore[no-redef]
        def __init__(self, state_type):
            self.state_type = state_type
            self.nodes = {}
            self.edges = []

        def add_node(self, name: str, func):
            self.nodes[name] = func

        def add_conditional_edges(self, source: str, condition_fn, mapping):
            self.edges.append((source, condition_fn, mapping))

        def compile(self):
            return self

        def invoke(self, state):
            for node_name, node_fn in self.nodes.items():
                if node_name not in ["triage", "data", "kpi", "prioritization", "retrieval", "playbook", "investigation", "planning", "action", "validation", "response"]:
                    continue
                state = node_fn(state)
            return state

from backend.app.agents.supervisor import run_supervisor
from backend.app.agents.triage import run_triage
from backend.app.agents.territory_data import run_territory_data
from backend.app.agents.kpi import run_kpi
from backend.app.agents.prioritization import run_prioritization
from backend.app.agents.retrieval import run_retrieval
from backend.app.agents.playbook import run_playbook
from backend.app.agents.investigation import run_investigation
from backend.app.agents.territory_planning import run_territory_planning
from backend.app.agents.next_best_action import run_next_best_action
from backend.app.agents.validator import run_validation
from backend.app.agents.response import run_response

MAX_RETRIES = 3


def route_validation(state: Dict[str, Any]) -> str:
    decision = str(state.get("validation_result", {}).get("decision", "PASS")).upper()
    if decision == "RETRY":
        return "retry"
    if decision == "HUMAN_REVIEW":
        return "human_review"
    return "complete"


def run_workflow(state: Dict[str, Any]) -> Dict[str, Any]:
    state.setdefault("retry_count", 0)
    state = run_supervisor(state)
    state = run_triage(state)
    state = run_territory_data(state)
    state = run_kpi(state)
    state = run_prioritization(state)
    state = run_retrieval(state)
    state = run_playbook(state)
    state = run_investigation(state)
    state = run_territory_planning(state)
    state = run_next_best_action(state)
    state = run_validation(state)
    decision = str(state.get("validation_result", {}).get("decision", "PASS")).upper()
    if decision == "RETRY" and state.get("retry_count", 0) < MAX_RETRIES:
        state["retry_count"] = int(state.get("retry_count", 0)) + 1
        return run_workflow(state)
    state = run_response(state)
    return state


def build_graph():
    try:
        graph = StateGraph(dict)
        graph.add_node("triage", run_triage)
        graph.add_node("supervisor", run_supervisor)
        graph.add_node("territory_data", run_territory_data)
        graph.add_node("kpi", run_kpi)
        graph.add_node("prioritization", run_prioritization)
        graph.add_node("retrieval", run_retrieval)
        graph.add_node("playbook", run_playbook)
        graph.add_node("investigation", run_investigation)
        graph.add_node("planning", run_territory_planning)
        graph.add_node("action", run_next_best_action)
        graph.add_node("validation", run_validation)
        graph.add_node("response", run_response)
        graph.add_conditional_edges("validation", route_validation, {"retry": "investigation", "human_review": "action", "complete": "response"})
        return graph.compile()
    except Exception:
        return None
