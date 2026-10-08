from __future__ import annotations

from typing import Any, Dict, List


def chunk_text(text: str, chunk_size: int = 800, overlap: int = 120) -> List[str]:
    if not text:
        return []
    chunks: List[str] = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks


def prepare_document_chunks(document: Dict[str, Any]) -> List[Dict[str, Any]]:
    chunks = []
    for index, chunk in enumerate(chunk_text(document["content"])):
        chunks.append({
            "document_id": document["document_id"],
            "chunk_index": index,
            "content": chunk,
            "metadata": {
                "title": document.get("title"),
                "source": document.get("source"),
                "category": document.get("category"),
                "territory": document.get("territory"),
                "product": document.get("product"),
                "version": document.get("version"),
                "effective_date": document.get("effective_date"),
                "access_level": document.get("access_level"),
            },
        })
    return chunks
