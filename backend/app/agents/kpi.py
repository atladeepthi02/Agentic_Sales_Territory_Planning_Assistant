from __future__ import annotations

from typing import Any, Dict


def run_kpi(state: Dict[str, Any]) -> Dict[str, Any]:
    accounts = state.get("account_data", [])
    kpis = {}
    for account in accounts:
        account_id = account.get("account_id")
        kpis[account_id] = {
            "account_id": account_id,
            "revenue_growth": float(account.get("growth_rate", 0.0)),
            "product_adoption": float(account.get("product_adoption", 0.0)),
            "opportunity_value": float(account.get("annual_revenue", 0.0)) * 0.2,
            "engagement_score": float(account.get("engagement_score", 0.5)),
            "risk_score": float(account.get("service_issues", 0)) / 5.0,
            "growth_potential": min(float(account.get("growth_rate", 0.0)) * 2.0, 1.0),
        }
    state["kpi_results"] = kpis
    return state
