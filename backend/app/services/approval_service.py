from __future__ import annotations

from typing import Any, Dict


def approval_required(action: Dict[str, Any]) -> bool:
    return bool(action.get("requires_approval") or action.get("action") in {"Schedule expansion meeting", "Create strategic opportunity"})
