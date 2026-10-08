from __future__ import annotations

from typing import Any, Dict, List, TypedDict


class AgentState(TypedDict, total=False):
    session_id: str
    user_id: str
    workflow_id: str
    user_query: str
    conversation_history: List[str]
    intent: Dict[str, Any]
    entities: Dict[str, Any]
    territory_data: Dict[str, Any]
    account_data: List[Dict[str, Any]]
    opportunity_data: List[Dict[str, Any]]
    activity_data: List[Dict[str, Any]]
    service_data: List[Dict[str, Any]]
    kpi_results: Dict[str, Any]
    prioritization_results: List[Dict[str, Any]]
    retrieved_documents: List[Dict[str, Any]]
    selected_playbooks: List[Dict[str, Any]]
    investigation_result: Dict[str, Any]
    territory_plan: Dict[str, Any]
    proposed_actions: List[Dict[str, Any]]
    tool_results: List[Dict[str, Any]]
    confidence: float
    validation_result: Dict[str, Any]
    human_approval: Dict[str, Any]
    errors: List[str]
    retry_count: int
    final_response: Dict[str, Any]
