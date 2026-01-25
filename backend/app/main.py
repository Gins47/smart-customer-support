import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.api.v1 import api_router
from contextlib import asynccontextmanager
from app.core.config import settings

os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY

@asynccontextmanager
async def lifespan(app:FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        print("✅ Database tables created")
    yield
    # Dispose engine on shutdown
    await engine.dispose()


app = FastAPI(title="Support AI agent",lifespan=lifespan)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  # Next.js
    ],
    allow_credentials=True,
    allow_methods=["*"],        # GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],        # Authorization, Content-Type, etc
)

@app.get("/")
async def root():
    return {"message": "AI Car Customer Service API is running."}


app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
