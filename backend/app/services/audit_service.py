from __future__ import annotations

from typing import Any, Dict


def log_audit(
    workflow_id: str,
    agent: str,
    decision: str,
    evidence: list[str] | str | None = None,
    account_id: str | None = None,
    territory_id: str | None = None,
    policy: str | None = None,
    confidence: float = 0.0,
    approval_status: str = "pending",
) -> Dict[str, Any]:
    entry = {
        "workflow_id": workflow_id,
        "account_id": account_id,
        "territory_id": territory_id,
        "agent": agent,
        "decision": decision,
        "evidence": evidence if isinstance(evidence, list) else [evidence] if evidence else [],
        "source_documents": [],
        "policy": policy,
        "confidence": confidence,
        "approval_status": approval_status,
    }
    return entry
