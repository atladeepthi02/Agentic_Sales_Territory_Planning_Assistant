from __future__ import annotations

from typing import Any, Dict


def run_response(state: Dict[str, Any]) -> Dict[str, Any]:
    actions = state.get("proposed_actions", [])
    final = {
        "facts": [
            f"Territory {state.get('intent', {}).get('territory_id') or 'T001'} analyzed.",
            f"{len(state.get('account_data', []))} accounts evaluated.",
        ],
        "analysis": [
            "Accounts with strongest growth potential and engagement were prioritized.",
            "Policy-backed recommendations are grounded in the retrieved sales playbook and territory rules.",
        ],
        "recommendations": [action["action"] for action in actions],
        "completed_actions": [],
        "pending_approval": actions,
        "sources": [item["document_id"] for item in state.get("retrieved_documents", [])],
    }
    state["final_response"] = final
    return state
