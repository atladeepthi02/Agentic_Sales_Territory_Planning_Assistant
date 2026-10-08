from __future__ import annotations

from typing import Any, Dict


def run_playbook(state: Dict[str, Any]) -> Dict[str, Any]:
    accounts = state.get("account_data", [])
    selected = []
    for account in accounts:
        score = next((item["priority_score"] for item in state.get("prioritization_results", []) if item["account_id"] == account["account_id"]), 0)
        playbook = "Expansion Playbook" if score >= 0.6 else "Retention Playbook"
        selected.append({"account_id": account["account_id"], "playbook": playbook, "reason": "Evidence-based sales fit", "confidence": 0.89})
    state["selected_playbooks"] = selected
    return state
