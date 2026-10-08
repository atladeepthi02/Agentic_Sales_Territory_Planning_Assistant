from __future__ import annotations

from typing import Any, Dict


def route_by_validation(validation: Dict[str, Any]) -> str:
    decision = str(validation.get("decision", "PASS")).upper()
    if decision == "RETRY":
        return "retry"
    if decision == "HUMAN_REVIEW":
        return "human_review"
    return "response"
