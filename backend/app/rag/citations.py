from __future__ import annotations

from typing import Any, Dict, List


def generate_citations(results: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    citations = []
    for item in results:
        metadata = item.get("metadata", {})
        citations.append({
            "document_id": metadata.get("document_id") or item.get("document_id"),
            "title": metadata.get("title") or item.get("title"),
            "source": metadata.get("source") or item.get("source"),
            "category": metadata.get("category"),
            "version": metadata.get("version"),
            "excerpt": item.get("content", "")[:220],
        })
    return citations
