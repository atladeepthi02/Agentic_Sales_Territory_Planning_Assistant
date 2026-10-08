from __future__ import annotations

from typing import Any, Dict, List

from backend.app.rag.loaders import load_documents_from_directory
from backend.app.rag.vector_store import vector_store


class Retriever:
    def __init__(self, directory: str = "data/knowledge_base"):
        self.directory = directory

    def ingest(self) -> List[Dict[str, Any]]:
        documents = load_documents_from_directory(self.directory)
        vector_store.add_documents(documents)
        return documents

    def search(self, query: str, limit: int = 5, metadata_filter: Dict[str, Any] | None = None) -> List[Dict[str, Any]]:
        return vector_store.search_documents(query=query, limit=limit, metadata_filter=metadata_filter)


retriever = Retriever()
