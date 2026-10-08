from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List


def load_documents_from_directory(directory: str) -> List[Dict[str, Any]]:
    base = Path(directory)
    documents: List[Dict[str, Any]] = []
    if not base.exists():
        return documents

    for file_path in sorted(base.rglob("*")):
        if file_path.is_file() and file_path.suffix.lower() in {".txt", ".md", ".csv"}:
            text = file_path.read_text(encoding="utf-8")
            documents.append(
                {
                    "document_id": file_path.stem,
                    "title": file_path.stem,
                    "source": str(file_path),
                    "content": text,
                    "category": "sales_policy",
                    "territory": "T001",
                    "product": "general",
                    "version": "v1",
                    "effective_date": "2026-01-01",
                    "access_level": "internal",
                }
            )
    return documents
