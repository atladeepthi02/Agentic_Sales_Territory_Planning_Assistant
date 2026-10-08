from __future__ import annotations

import json
from typing import Any, Dict, List

try:
    import chromadb
except Exception:  # pragma: no cover
    chromadb = None

from backend.app.rag.embeddings import deterministic_embedding


class VectorStore:
    def __init__(self, collection_name: str = "sales_policy"):
        self.collection_name = collection_name
        self.client = None
        self.collection = None
        if chromadb is not None:
            try:
                self.client = chromadb.Client()
                self.collection = self.client.get_or_create_collection(name=collection_name)
            except Exception:
                self.client = None
                self.collection = None

    def add_documents(self, documents: List[Dict[str, Any]]) -> None:
        if self.collection is None:
            return
        ids = []
        embeds = []
        metas = []
        for idx, doc in enumerate(documents):
            ids.append(f"{doc['document_id']}-{idx}")
            embeds.append(deterministic_embedding(doc["content"]))
            metas.append({
                "document_id": doc.get("document_id"),
                "title": doc.get("title"),
                "source": doc.get("source"),
                "category": doc.get("category"),
                "territory": doc.get("territory"),
                "product": doc.get("product"),
                "version": doc.get("version"),
                "effective_date": doc.get("effective_date"),
                "access_level": doc.get("access_level"),
            })
        self.collection.add(ids=ids, embeddings=embeds, metadatas=metas, documents=[d["content"] for d in documents])

    def search_documents(self, query: str, limit: int = 5, metadata_filter: Dict[str, Any] | None = None) -> List[Dict[str, Any]]:
        if self.collection is None:
            return []
        query_embedding = deterministic_embedding(query)
        kwargs = {"query_embeddings": [query_embedding], "n_results": limit}
        if metadata_filter:
            kwargs["where"] = metadata_filter
        results = self.collection.query(**kwargs)
        output = []
        for i in range(len(results.get("documents", [[]])[0])):
            output.append({
                "document_id": results["metadatas"][0][i].get("document_id"),
                "title": results["metadatas"][0][i].get("title"),
                "source": results["metadatas"][0][i].get("source"),
                "content": results["documents"][0][i],
                "metadata": results["metadatas"][0][i],
            })
        return output

    def search_by_metadata(self, metadata_filter: Dict[str, Any], limit: int = 5) -> List[Dict[str, Any]]:
        return self.search_documents("", limit=limit, metadata_filter=metadata_filter)

    def delete_document(self, document_id: str) -> None:
        if self.collection is not None:
            self.collection.delete(where={"document_id": document_id})

    def update_document(self, document_id: str, document: Dict[str, Any]) -> None:
        self.delete_document(document_id)
        self.add_documents([document])


vector_store = VectorStore()
