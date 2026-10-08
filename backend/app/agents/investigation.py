from __future__ import annotations

from typing import Any, Dict


def run_investigation(state: Dict[str, Any]) -> Dict[str, Any]:
    prioritized = state.get("prioritization_results", [])
    account = prioritized[0] if prioritized else {"account_id": "ACC1025"}
    evidence = [
        "Revenue growth above benchmark threshold",
        "Open expansion opportunity exists",
        "Product adoption is strong enough to justify follow-up",
    ]
    state["investigation_result"] = {
        "account_id": account.get("account_id"),
        "issue_type": "EXPANSION_OPPORTUNITY",
        "evidence": evidence,
        "policy_reference": ["PLAYBOOK-EXP-001"],
        "recommended_action": "Schedule expansion discussion",
        "confidence": 0.91,
        "requires_human_review": True,
    }
    return state
