from __future__ import annotations

from typing import Any, Dict

from backend.app.data.mock_store import ACCOUNTS, ACTIVITIES, OPPORTUNITIES, SERVICE_ISSUES, TERRITORIES
from backend.app.tools.territory_tools import get_accounts_by_territory, get_territory


def run_territory_data(state: Dict[str, Any]) -> Dict[str, Any]:
    territory_id = state.get("intent", {}).get("territory_id") or "T001"
    territory = get_territory(territory_id)
    accounts = get_accounts_by_territory(territory_id)
    opportunities = [o for o in OPPORTUNITIES if o.get("account_id") in {a["account_id"] for a in accounts}]
    activities = [a for a in ACTIVITIES if a.get("account_id") in {a["account_id"] for a in accounts}]
    service_data = [s for s in SERVICE_ISSUES if s.get("account_id") in {a["account_id"] for a in accounts}]

    state["territory_data"] = territory
    state["account_data"] = accounts
    state["opportunity_data"] = opportunities
    state["activity_data"] = activities
    state["service_data"] = service_data
    return state
