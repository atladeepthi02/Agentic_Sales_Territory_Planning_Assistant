from __future__ import annotations

from typing import Any, Dict


def run_validation(state: Dict[str, Any]) -> Dict[str, Any]:
    actions = state.get("proposed_actions", [])
    if not actions:
        state["validation_result"] = {"decision": "PASS", "reason": "No actions pending", "policy_compliant": True, "evidence_sufficient": True, "confidence": 0.9}
        return state
    state["validation_result"] = {
        "decision": "HUMAN_REVIEW",
        "reason": "Recommended action modifies account engagement strategy and requires manager approval",
        "policy_compliant": True,
        "evidence_sufficient": True,
        "confidence": 0.88,
    }
    return state
