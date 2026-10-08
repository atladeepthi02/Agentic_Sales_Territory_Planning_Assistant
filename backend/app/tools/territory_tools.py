from __future__ import annotations

from typing import Any, Dict, List

from backend.app.data.mock_store import ACCOUNTS, ACTIVITIES, CONTACTS, OPPORTUNITIES, SERVICE_ISSUES, TERRITORIES


def get_territory(territory_id: str) -> Dict[str, Any]:
    return TERRITORIES.get(territory_id, {})


def get_accounts_by_territory(territory_id: str) -> List[Dict[str, Any]]:
    return [a for a in ACCOUNTS if a.get("territory_id") == territory_id]


def get_account(account_id: str) -> Dict[str, Any]:
    for account in ACCOUNTS:
        if account["account_id"] == account_id:
            return account
    return {}


def get_account_history(account_id: str) -> List[Dict[str, Any]]:
    return [a for a in ACTIVITIES if a.get("account_id") == account_id]


def get_account_revenue(account_id: str) -> float:
    account = get_account(account_id)
    return float(account.get("annual_revenue", 0.0))


def get_product_adoption(account_id: str) -> float:
    account = get_account(account_id)
    return float(account.get("product_adoption", 0.0))


def get_opportunities(account_id: str | None = None) -> List[Dict[str, Any]]:
    if account_id:
        return [o for o in OPPORTUNITIES if o.get("account_id") == account_id]
    return OPPORTUNITIES


def get_sales_activities(account_id: str | None = None) -> List[Dict[str, Any]]:
    if account_id:
        return [a for a in ACTIVITIES if a.get("account_id") == account_id]
    return ACTIVITIES


def get_service_issues(account_id: str | None = None) -> List[Dict[str, Any]]:
    if account_id:
        return [issue for issue in SERVICE_ISSUES if issue.get("account_id") == account_id]
    return SERVICE_ISSUES


def get_account_contacts(account_id: str | None = None) -> List[Dict[str, Any]]:
    if account_id:
        return [c for c in CONTACTS if c.get("account_id") == account_id]
    return CONTACTS


def get_territory_rules(territory_id: str) -> List[str]:
    territory = TERRITORIES.get(territory_id, {})
    return territory.get("rules", [])
