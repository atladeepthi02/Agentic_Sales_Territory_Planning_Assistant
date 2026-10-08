from __future__ import annotations

from typing import Any, Dict, List


def build_context(results: List[Dict[str, Any]]) -> str:
    lines = []
    for item in results:
        metadata = item.get("metadata", {})
        lines.append(
            f"Source: {metadata.get('title', 'Unknown')} | Category: {metadata.get('category', 'unknown')} | "
            f"Version: {metadata.get('version', 'n/a')} | Excerpt: {item.get('content', '')[:300]}"
        )
    return "\n".join(lines)
