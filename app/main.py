"""FastAPI app serving a simple streaming chat UI backed by a local Ollama model."""
from fastapi import FastAPI
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.ollama_client import stream_chat

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# In-memory conversation history per session; lost on restart.
_sessions: dict[str, list[dict]] = {}


class ChatRequest(BaseModel):
    session_id: str
    message: str


@app.get("/")
async def index():
    return FileResponse("app/static/index.html")


@app.post("/api/chat")
async def chat(req: ChatRequest):
    history = _sessions.setdefault(req.session_id, [])
    history.append({"role": "user", "content": req.message})

    async def event_stream():
        reply_parts: list[str] = []
        async for chunk in stream_chat(history):
            reply_parts.append(chunk)
            yield chunk
        history.append({"role": "assistant", "content": "".join(reply_parts)})

    return StreamingResponse(event_stream(), media_type="text/plain")
