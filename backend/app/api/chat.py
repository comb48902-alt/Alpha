from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.core.ai import chat_with_m

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    history: list = []

@router.post("/chat")
async def chat(req: ChatRequest):
    reply = await chat_with_m(req.message, req.history)
    return {"reply": reply, "assistant": "M"}
