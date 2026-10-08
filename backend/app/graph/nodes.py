from __future__ import annotations

from typing import Any, Dict


def triage_node(state: Dict[str, Any]) -> Dict[str, Any]:
    return {"intent": {"intent": "territory_prioritization"}, "confidence": 0.9}


def data_node(state: Dict[str, Any]) -> Dict[str, Any]:
    return {"territory_data": {"territory_id": "T001"}, "account_data": [], "opportunity_data": [], "activity_data": [], "service_data": []}


def response_node(state: Dict[str, Any]) -> Dict[str, Any]:
    return {"final_response": {"facts": ["Workflow completed"], "analysis": ["Deterministic baseline response generated"], "recommendations": [], "completed_actions": [], "pending_approval": [], "sources": []}}
