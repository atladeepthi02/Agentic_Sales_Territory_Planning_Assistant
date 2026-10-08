from __future__ import annotations

from typing import Any, Dict


def should_retry(state: Dict[str, Any]) -> bool:
    return int(state.get("retry_count", 0)) < 3
