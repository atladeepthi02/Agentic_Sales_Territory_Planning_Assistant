from __future__ import annotations

import os
from typing import Any, Dict

from backend.app.config.settings import settings


async def generate_text(prompt: str, system_message: str | None = None) -> Dict[str, Any]:
    if not settings.openai_api_key:
        return {
            "content": (
                "OpenAI API key is not configured. Returning a deterministic fallback response for local development."
            ),
            "provider": "fallback",
            "model": settings.openai_model,
        }

    try:
        from openai import AsyncOpenAI

        client = AsyncOpenAI(api_key=settings.openai_api_key)
        response = await client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {"role": "system", "content": system_message or "You are a careful sales planning assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.1,
            max_tokens=800,
        )
        content = response.choices[0].message.content or ""
        return {"content": content, "provider": "openai", "model": settings.openai_model}
    except Exception as exc:  # pragma: no cover
        return {
            "content": f"LLM generation failed: {exc}. Falling back to deterministic output.",
            "provider": "fallback",
            "model": settings.openai_model,
        }
