from __future__ import annotations

from typing import Any, Dict

from backend.app.data.mock_store import POLICIES


def run_retrieval(state: Dict[str, Any]) -> Dict[str, Any]:
    query = state.get("user_query", "")
    documents = [
        {"document_id": policy["document_id"], "title": policy["title"], "source": policy["source"], "content": policy["content"], "metadata": policy}
        for policy in POLICIES
        if "expansion" in query.lower() or "plan" in query.lower() or "policy" in query.lower() or "territory" in query.lower()
    ]
    if not documents:
        documents = [{"document_id": policy["document_id"], "title": policy["title"], "source": policy["source"], "content": policy["content"], "metadata": policy} for policy in POLICIES]
    state["retrieved_documents"] = documents
    return state
