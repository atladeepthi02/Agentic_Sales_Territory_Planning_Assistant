from __future__ import annotations

from typing import Any, Dict


def run_supervisor(state: Dict[str, Any]) -> Dict[str, Any]:
    query = str(state.get("user_query", "")).lower()
    if "territory" in query or "plan" in query:
        state["intent"] = {"intent": "territory_prioritization", "category": "sales_planning"}
    elif "account" in query or "top" in query:
        state["intent"] = {"intent": "account_prioritization", "category": "sales_planning"}
    else:
        state["intent"] = {"intent": "general_analysis", "category": "sales_planning"}
    state.setdefault("errors", [])
    return state
