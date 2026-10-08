from __future__ import annotations

from backend.app.data.mock_store import POLICIES
from backend.app.rag.vector_store import vector_store

for policy in POLICIES:
    vector_store.add_documents([{
        "document_id": policy["document_id"],
        "title": policy["title"],
        "source": policy["source"],
        "content": policy["content"],
        "category": policy["category"],
        "territory": policy["territory"],
        "product": policy["product"],
        "version": policy["version"],
        "effective_date": policy["effective_date"],
        "access_level": policy["access_level"],
    }])

print("Ingestion complete")
