from __future__ import annotations

TERRITORIES = {
    "T001": {
        "territory_id": "T001",
        "name": "North Region",
        "manager": "Maya Chen",
        "region": "Northeast",
        "rules": ["Review at-risk accounts weekly", "Expansion approvals require manager sign-off"],
    },
    "T002": {
        "territory_id": "T002",
        "name": "Midwest Region",
        "manager": "Alex Rivera",
        "region": "Central",
        "rules": ["Call plans due every Tuesday", "Escalate any customer outage above severity 1"],
    },
}

ACCOUNTS = [
    {
        "account_id": "ACC1025",
        "account_name": "ABC Retail",
        "territory_id": "T001",
        "annual_revenue": 1250000,
        "growth_rate": 0.18,
        "product_adoption": 0.72,
        "open_opportunities": 3,
        "service_issues": 1,
        "last_contact_date": "2026-09-20",
        "health_score": 0.86,
        "engagement_score": 0.81,
        "owner": "Maya Chen",
    },
    {
        "account_id": "ACC1040",
        "account_name": "ValueMart",
        "territory_id": "T001",
        "annual_revenue": 980000,
        "growth_rate": 0.11,
        "product_adoption": 0.58,
        "open_opportunities": 1,
        "service_issues": 3,
        "last_contact_date": "2026-08-10",
        "health_score": 0.62,
        "engagement_score": 0.61,
        "owner": "Maya Chen",
    },
    {
        "account_id": "ACC1088",
        "account_name": "Summit Foods",
        "territory_id": "T001",
        "annual_revenue": 2100000,
        "growth_rate": 0.09,
        "product_adoption": 0.81,
        "open_opportunities": 5,
        "service_issues": 0,
        "last_contact_date": "2026-09-25",
        "health_score": 0.9,
        "engagement_score": 0.88,
        "owner": "Maya Chen",
    },
    {
        "account_id": "ACC1111",
        "account_name": "Aster Supply",
        "territory_id": "T002",
        "annual_revenue": 880000,
        "growth_rate": 0.06,
        "product_adoption": 0.49,
        "open_opportunities": 2,
        "service_issues": 2,
        "last_contact_date": "2026-09-04",
        "health_score": 0.54,
        "engagement_score": 0.5,
        "owner": "Alex Rivera",
    },
]

OPPORTUNITIES = [
    {"opportunity_id": "OP-1001", "account_id": "ACC1025", "amount": 250000, "probability": 0.75, "stage": "DISCOVERY"},
    {"opportunity_id": "OP-1002", "account_id": "ACC1025", "amount": 180000, "probability": 0.68, "stage": "PROPOSAL"},
    {"opportunity_id": "OP-1003", "account_id": "ACC1088", "amount": 440000, "probability": 0.82, "stage": "NEGOTIATION"},
    {"opportunity_id": "OP-1004", "account_id": "ACC1040", "amount": 98000, "probability": 0.42, "stage": "QUALIFY"},
]

ACTIVITIES = [
    {"activity_id": "ACT-1001", "account_id": "ACC1025", "activity_type": "call", "activity_date": "2026-09-20", "notes": "Discussed expansion roadmap."},
    {"activity_id": "ACT-1002", "account_id": "ACC1040", "activity_type": "email", "activity_date": "2026-08-10", "notes": "Follow-up on support issue."},
]

SERVICE_ISSUES = [
    {"issue_id": "SI-1001", "account_id": "ACC1040", "severity": "HIGH", "summary": "Recurring outage in point-of-sale module", "created_at": "2026-09-12"},
    {"issue_id": "SI-1002", "account_id": "ACC1025", "severity": "LOW", "summary": "Minor configuration issue", "created_at": "2026-09-18"},
]

CONTACTS = [
    {"contact_id": "CT-1001", "account_id": "ACC1025", "name": "Jamie Lee", "role": "VP Retail", "email": "jamie.lee@abcretail.com", "last_contact": "2026-09-20"},
    {"contact_id": "CT-1002", "account_id": "ACC1040", "name": "Parker Dunn", "role": "Operations Lead", "email": "parker@valuemart.com", "last_contact": "2026-08-10"},
]

POLICIES = [
    {
        "document_id": "PLAYBOOK-EXP-001",
        "title": "Expansion Playbook",
        "source": "sales_playbooks/expansion.md",
        "content": "When a customer has revenue growth above 15%, product adoption above 70%, and an open expansion opportunity, use the Expansion Playbook. Schedule a strategic account review within 10 business days and validate pricing expectations with manager approval.",
        "category": "sales_playbook",
        "territory": "T001",
        "product": "general",
        "version": "v3",
        "effective_date": "2026-01-12",
        "access_level": "internal",
    },
    {
        "document_id": "TERRITORY-POLICY-001",
        "title": "Territory Ownership Policy",
        "source": "territory_policies/ownership.md",
        "content": "Account actions must remain within assigned territory ownership and require explicit authorization for any cross-territory changes or strategic account modifications.",
        "category": "territory_policy",
        "territory": "T001",
        "product": "general",
        "version": "v2",
        "effective_date": "2026-01-01",
        "access_level": "internal",
    }
]
