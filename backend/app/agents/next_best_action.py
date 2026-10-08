from __future__ import annotations

from typing import Any, Dict, List


def run_next_best_action(state: Dict[str, Any]) -> Dict[str, Any]:
    actions: List[Dict[str, Any]] = []
    for account in state.get("account_data", [])[:2]:
        actions.append({
            "account_id": account["account_id"],
            "action": "Schedule expansion meeting",
            "reason": "High growth and expansion opportunity",
            "expected_outcome": "Increase product adoption and pipeline strength",
            "confidence": 0.9,
            "evidence": ["Revenue growth is above 15%", "Open expansion opportunity exists"],
            "requires_approval": True,
        })
    state["proposed_actions"] = actions
    return state
