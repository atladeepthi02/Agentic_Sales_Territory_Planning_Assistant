from __future__ import annotations

from typing import Any, Dict, List


def rerank_results(results: List[Dict[str, Any]], query: str) -> List[Dict[str, Any]]:
    ranked = []
    for result in results:
        score = 0.0
        content = str(result.get("content", "")).lower()
        if query.lower() in content:
            score += 0.3
        if "policy" in str(result.get("metadata", {})).lower():
            score += 0.2
        if "expansion" in content:
            score += 0.1
        ranked.append({**result, "score": round(score, 3)})
    ranked.sort(key=lambda item: item.get("score", 0.0), reverse=True)
    return ranked
