from __future__ import annotations

import re
from typing import Any, Dict


def run_triage(state: Dict[str, Any]) -> Dict[str, Any]:
    query = state.get("user_query", "")
    territory = re.search(r"T\d+", query, flags=re.I)
    account = re.search(r"ACC\d+", query, flags=re.I)
    state["intent"] = {
        "intent": "territory_prioritization",
        "category": "sales_planning",
        "territory_id": territory.group(0) if territory else None,
        "account_id": account.group(0) if account else None,
        "time_period": "Q4",
        "priority": "HIGH",
        "entities": {"territory_id": territory.group(0) if territory else None, "account_id": account.group(0) if account else None},
        "missing_information": [],
        "confidence": 0.92,
        "recommended_route": "territory_analysis",
    }
    return state
