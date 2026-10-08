from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(100), default="sales_manager")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Territory(Base):
    __tablename__ = "territories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    territory_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    manager: Mapped[str] = mapped_column(String(255), nullable=True)
    region: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    accounts: Mapped[List["Account"]] = relationship(back_populates="territory")


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    account_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    account_name: Mapped[str] = mapped_column(String(255))
    territory_id: Mapped[str] = mapped_column(String(50), ForeignKey("territories.territory_id"))
    annual_revenue: Mapped[float] = mapped_column(Float, default=0.0)
    growth_rate: Mapped[float] = mapped_column(Float, default=0.0)
    product_adoption: Mapped[float] = mapped_column(Float, default=0.0)
    open_opportunities: Mapped[int] = mapped_column(Integer, default=0)
    service_issues: Mapped[int] = mapped_column(Integer, default=0)
    last_contact_date: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    health_score: Mapped[float] = mapped_column(Float, default=0.0)
    owner: Mapped[str] = mapped_column(String(255), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    territory: Mapped["Territory"] = relationship(back_populates="accounts")
    opportunities: Mapped[List["Opportunity"]] = relationship(back_populates="account")
    activities: Mapped[List["SalesActivity"]] = relationship(back_populates="account")
    service_issues_list: Mapped[List["ServiceIssue"]] = relationship(back_populates="account")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    product_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    category: Mapped[str] = mapped_column(String(255), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class Opportunity(Base):
    __tablename__ = "opportunities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    opportunity_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    account_id: Mapped[str] = mapped_column(String(50), ForeignKey("accounts.account_id"))
    product_id: Mapped[str] = mapped_column(String(50), ForeignKey("products.product_id"), nullable=True)
    stage: Mapped[str] = mapped_column(String(120), default="QUALIFY")
    amount: Mapped[float] = mapped_column(Float, default=0.0)
    probability: Mapped[float] = mapped_column(Float, default=0.0)
    expected_close_date: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    account: Mapped["Account"] = relationship(back_populates="opportunities")


class SalesActivity(Base):
    __tablename__ = "sales_activities"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    activity_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    account_id: Mapped[str] = mapped_column(String(50), ForeignKey("accounts.account_id"))
    activity_type: Mapped[str] = mapped_column(String(150))
    notes: Mapped[str] = mapped_column(Text)
    activity_date: Mapped[str] = mapped_column(String(50))

    account: Mapped["Account"] = relationship(back_populates="activities")


class ServiceIssue(Base):
    __tablename__ = "service_issues"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    issue_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    account_id: Mapped[str] = mapped_column(String(50), ForeignKey("accounts.account_id"))
    severity: Mapped[str] = mapped_column(String(50), default="MEDIUM")
    summary: Mapped[str] = mapped_column(Text)
    created_at: Mapped[str] = mapped_column(String(50))

    account: Mapped["Account"] = relationship(back_populates="service_issues_list")


class AccountContact(Base):
    __tablename__ = "account_contacts"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    contact_id: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    account_id: Mapped[str] = mapped_column(String(50), ForeignKey("accounts.account_id"))
    name: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    last_contact: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    session_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    user_id: Mapped[str] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Message(Base):
    __tablename__ = "messages"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    session_id: Mapped[str] = mapped_column(String(100), ForeignKey("sessions.session_id"))
    role: Mapped[str] = mapped_column(String(50))
    content: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Workflow(Base):
    __tablename__ = "workflows"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workflow_id: Mapped[str] = mapped_column(String(120), unique=True, index=True)
    session_id: Mapped[str] = mapped_column(String(100), nullable=True)
    user_id: Mapped[str] = mapped_column(String(100), nullable=True)
    status: Mapped[str] = mapped_column(String(60), default="started")
    current_node: Mapped[str] = mapped_column(String(120), default="triage")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    started_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    completed_at: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)


class AgentRun(Base):
    __tablename__ = "agent_runs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workflow_id: Mapped[str] = mapped_column(String(120), ForeignKey("workflows.workflow_id"))
    agent_name: Mapped[str] = mapped_column(String(150))
    status: Mapped[str] = mapped_column(String(60), default="success")
    latency_ms: Mapped[int] = mapped_column(Integer, default=0)
    model_name: Mapped[str] = mapped_column(String(120), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class ToolCall(Base):
    __tablename__ = "tool_calls"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workflow_id: Mapped[str] = mapped_column(String(120), ForeignKey("workflows.workflow_id"))
    tool_name: Mapped[str] = mapped_column(String(150))
    arguments: Mapped[str] = mapped_column(Text)
    result: Mapped[str] = mapped_column(Text)
    success: Mapped[bool] = mapped_column(Integer, default=1)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(255))
    source: Mapped[str] = mapped_column(String(255), nullable=True)
    category: Mapped[str] = mapped_column(String(120), nullable=True)
    territory: Mapped[str] = mapped_column(String(50), nullable=True)
    product: Mapped[str] = mapped_column(String(100), nullable=True)
    version: Mapped[str] = mapped_column(String(50), nullable=True)
    effective_date: Mapped[str] = mapped_column(String(50), nullable=True)
    access_level: Mapped[str] = mapped_column(String(50), default="internal")
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class DocumentChunk(Base):
    __tablename__ = "document_chunks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    document_id: Mapped[str] = mapped_column(String(100), ForeignKey("documents.document_id"))
    chunk_index: Mapped[int] = mapped_column(Integer, default=0)
    content: Mapped[str] = mapped_column(Text)
    metadata_json: Mapped[str] = mapped_column(Text, default="{}")


class Playbook(Base):
    __tablename__ = "playbooks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    playbook_id: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str] = mapped_column(Text)
    category: Mapped[str] = mapped_column(String(120), default="sales")


class Approval(Base):
    __tablename__ = "approvals"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workflow_id: Mapped[str] = mapped_column(String(120), ForeignKey("workflows.workflow_id"))
    account_id: Mapped[str] = mapped_column(String(50), nullable=True)
    action: Mapped[str] = mapped_column(String(200))
    status: Mapped[str] = mapped_column(String(50), default="pending")
    requested_by: Mapped[str] = mapped_column(String(150), nullable=True)
    approved_by: Mapped[str] = mapped_column(String(150), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class AuditLog(Base):
    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workflow_id: Mapped[str] = mapped_column(String(120), ForeignKey("workflows.workflow_id"))
    account_id: Mapped[str] = mapped_column(String(50), nullable=True)
    territory_id: Mapped[str] = mapped_column(String(50), nullable=True)
    agent: Mapped[str] = mapped_column(String(150))
    decision: Mapped[str] = mapped_column(String(150))
    evidence: Mapped[str] = mapped_column(Text)
    source_documents: Mapped[str] = mapped_column(Text)
    policy: Mapped[str] = mapped_column(String(255), nullable=True)
    confidence: Mapped[float] = mapped_column(Float, default=0.0)
    approval_status: Mapped[str] = mapped_column(String(60), default="pending")
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)


class Evaluation(Base):
    __tablename__ = "evaluations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    workflow_id: Mapped[str] = mapped_column(String(120), ForeignKey("workflows.workflow_id"))
    scenario: Mapped[str] = mapped_column(String(255))
    score: Mapped[float] = mapped_column(Float, default=0.0)
    details: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
