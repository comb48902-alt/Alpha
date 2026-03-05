from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.chat import router as chat_router

app = FastAPI(title="ALPHA+OMEGA", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api")

@app.get("/")
def root():
    return {"status": "ALPHA+OMEGA online", "assistant": "M"}

@app.get("/health")
def health():
    return {"status": "ok"}
