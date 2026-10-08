import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from backend.app.graph.workflow import run_workflow


def test_run_workflow_returns_final_response():
    state = {
        "session_id": "s-1",
        "user_id": "u-1",
        "workflow_id": "w-1",
        "user_query": "Analyze territory T001 and identify the top accounts",
        "conversation_history": [],
        "retry_count": 0,
        "errors": [],
    }
    result = run_workflow(state)
    assert "final_response" in result
    assert result["validation_result"]["decision"] in {"HUMAN_REVIEW", "PASS"}
