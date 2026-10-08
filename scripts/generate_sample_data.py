from __future__ import annotations

from pathlib import Path

root = Path(__file__).resolve().parent.parent
knowledge_dir = root / "data" / "knowledge_base"
knowledge_dir.mkdir(parents=True, exist_ok=True)

playbook = knowledge_dir / "sales_playbooks" / "expansion.md"
playbook.parent.mkdir(parents=True, exist_ok=True)
playbook.write_text(
    "# Expansion Playbook\n\n"
    "When a customer has revenue growth above 15%, product adoption above 70%, and a valid expansion opportunity, use the Expansion Playbook.\n"
    "Schedule a strategic account review within 10 business days and validate pricing with manager sign-off.\n",
    encoding="utf-8",
)

policy = knowledge_dir / "territory_policies" / "ownership.md"
policy.parent.mkdir(parents=True, exist_ok=True)
policy.write_text(
    "# Territory Ownership Policy\n\n"
    "Account actions must remain within assigned territory ownership. Cross-territory changes require explicit authorization and manager approval.\n",
    encoding="utf-8",
)

print("Sample data generated")
