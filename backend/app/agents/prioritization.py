from __future__ import annotations

from typing import Any, Dict, List

from backend.app.services.scoring_service import calculate_priority_score


def run_prioritization(state: Dict[str, Any]) -> Dict[str, Any]:
    results: List[Dict[str, Any]] = []
    for account in state.get("account_data", []):
        opportunities = [op for op in state.get("opportunity_data", []) if op.get("account_id") == account.get("account_id")]
        result = calculate_priority_score(account, opportunities)
        results.append(result)
    results.sort(key=lambda item: item["priority_score"], reverse=True)
    state["prioritization_results"] = results
    return state
