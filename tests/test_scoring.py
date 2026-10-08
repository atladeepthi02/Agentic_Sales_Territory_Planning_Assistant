import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.app.services.scoring_service import calculate_priority_score


def test_priority_score_ranks_high_growth_account():
    account = {
        "account_id": "ACC1025",
        "growth_rate": 0.18,
        "product_adoption": 0.72,
        "engagement_score": 0.81,
        "health_score": 0.86,
        "service_issues": 1,
    }
    score = calculate_priority_score(account, [{"amount": 250000}])
    assert score["priority"] == "HIGH"
    assert score["priority_score"] > 0.6
