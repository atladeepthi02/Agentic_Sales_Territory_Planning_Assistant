from __future__ import annotations

import uuid
from typing import Any, Dict, List

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from backend.app.data.mock_store import ACCOUNTS, TERRITORIES
from backend.app.graph.workflow import run_workflow
from backend.app.tools.territory_tools import get_account, get_accounts_by_territory, get_territory

app = FastAPI(title="Agentic Sales Territory Planning Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    user_query: str
    session_id: str | None = None
    user_id: str | None = None


class ApprovalRequest(BaseModel):
    approved: bool = True
    notes: str | None = None


@app.get("/api/health")
async def health() -> Dict[str, Any]:
    return {"status": "ok", "service": "backend", "timestamp": "2026-10-08T00:00:00Z"}


@app.get("/api/metrics")
async def metrics() -> Dict[str, Any]:
    return {"workflows": 1, "accounts": len(ACCOUNTS), "territories": len(TERRITORIES)}


@app.post("/api/chat")
async def chat(request: ChatRequest) -> Dict[str, Any]:
    workflow_id = str(uuid.uuid4())
    state = {
        "session_id": request.session_id or str(uuid.uuid4()),
        "user_id": request.user_id or "sales-manager",
        "workflow_id": workflow_id,
        "user_query": request.user_query,
        "conversation_history": [request.user_query],
        "retry_count": 0,
        "errors": [],
    }
    result = run_workflow(state)
    return {"workflow_id": workflow_id, "response": result.get("final_response", {}), "validation": result.get("validation_result", {})}


@app.post("/api/agent/run")
async def agent_run(request: ChatRequest) -> Dict[str, Any]:
    workflow_id = str(uuid.uuid4())
    state = {
        "session_id": request.session_id or str(uuid.uuid4()),
        "user_id": request.user_id or "sales-manager",
        "workflow_id": workflow_id,
        "user_query": request.user_query,
        "conversation_history": [request.user_query],
    }
    output = run_workflow(state)
    return {"workflow_id": workflow_id, "state": output}


@app.post("/api/territories/analyze")
async def analyze_territory(payload: Dict[str, Any]) -> Dict[str, Any]:
    territory_id = payload.get("territory_id", "T001")
    territory = get_territory(territory_id)
    accounts = get_accounts_by_territory(territory_id)
    if not territory:
        raise HTTPException(status_code=404, detail="Territory not found")
    return {"territory": territory, "accounts": accounts, "summary": {"total_accounts": len(accounts), "revenue": sum(float(a.get("annual_revenue", 0)) for a in accounts)}}


@app.post("/api/territories/{territory_id}/plan")
async def territory_plan(territory_id: str) -> Dict[str, Any]:
    return {
        "territory_id": territory_id,
        "plan": {
            "summary": {"total_accounts": 3, "revenue": 4_300_000, "growth": 0.13},
            "priority_accounts": ["ACC1025", "ACC1088"],
            "strategy": ["Focus on expansion accounts", "Review high-risk accounts"],
        }
    }


@app.post("/api/accounts/{account_id}/analyze")
async def account_analyze(account_id: str) -> Dict[str, Any]:
    account = get_account(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return {"account": account, "recommendation": "Schedule expansion review"}


@app.get("/api/sessions/{session_id}")
async def get_session(session_id: str) -> Dict[str, Any]:
    return {"session_id": session_id, "history": []}


@app.get("/api/workflows/{workflow_id}")
async def get_workflow(workflow_id: str) -> Dict[str, Any]:
    return {"workflow_id": workflow_id, "status": "completed"}


@app.post("/api/approval/{workflow_id}")
async def approval(workflow_id: str, payload: ApprovalRequest) -> Dict[str, Any]:
    return {"workflow_id": workflow_id, "status": "approved" if payload.approved else "rejected", "notes": payload.notes}


@app.post("/api/documents/upload")
async def upload_document() -> Dict[str, Any]:
    return {"status": "uploaded"}


@app.post("/api/documents/ingest")
async def ingest_document() -> Dict[str, Any]:
    return {"status": "ingested"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="0.0.0.0", port=8000, reload=True)
