from __future__ import annotations

from typing import Any, Dict, List


def calculate_priority_score(account: Dict[str, Any], opportunities: List[Dict[str, Any]] | None = None) -> Dict[str, Any]:
    growth = float(account.get("growth_rate", 0.0))
    opportunity_value = sum(float(item.get("amount", 0.0)) for item in (opportunities or []))
    adoption = float(account.get("product_adoption", 0.0))
    engagement = float(account.get("engagement_score", 0.5))
    service_risk = float(account.get("service_issues", 0))
    health = float(account.get("health_score", 0.5))

    growth_component = min(max(growth / 0.20, 0.0), 1.0)
    opportunity_component = min(opportunity_value / 300_000.0, 1.0)
    adoption_component = min(max(adoption / 0.8, 0.0), 1.0)
    engagement_component = min(max(engagement, 0.0), 1.0)
    health_component = min(max(health, 0.0), 1.0)
    risk_penalty = min(service_risk / 10.0, 0.25)

    score = (
        0.40 * growth_component
        + 0.25 * opportunity_component
        + 0.20 * adoption_component
        + 0.15 * engagement_component
        + 0.10 * health_component
        - risk_penalty
    )

    score = max(0.0, min(score, 1.0))
    priority = "LOW"
    if score >= 0.75:
        priority = "HIGH"
    elif score >= 0.5:
        priority = "MEDIUM"

    reason_codes = []
    if growth > 0.12:
        reason_codes.append("HIGH_GROWTH")
    if opportunity_value > 100000:
        reason_codes.append("OPEN_EXPANSION_OPPORTUNITY")
    if adoption < 0.7:
        reason_codes.append("LOW_PRODUCT_ADOPTION_GAP")
    if service_risk > 0:
        reason_codes.append("SERVICE_ISSUE")

    return {
        "account_id": account.get("account_id"),
        "priority_score": round(score, 3),
        "priority": priority,
        "reason_codes": reason_codes,
    }
