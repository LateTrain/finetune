"""Thin streaming wrapper around Ollama's local /api/chat endpoint."""
import json
from typing import AsyncIterator

import httpx

OLLAMA_BASE_URL = "http://localhost:11434"
MODEL_NAME = "finetune-poc"


async def stream_chat(messages: list[dict]) -> AsyncIterator[str]:
    """Yield response text chunks as they arrive from Ollama."""
    payload = {"model": MODEL_NAME, "messages": messages, "stream": True}
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream(
            "POST", f"{OLLAMA_BASE_URL}/api/chat", json=payload
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_lines():
                if not line:
                    continue
                data = json.loads(line)
                content = data.get("message", {}).get("content", "")
                if content:
                    yield content
                if data.get("done"):
                    break
