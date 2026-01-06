import os
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession

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

# --------------------------
# Dependency: Async DB session
# --------------------------
async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session


# --------------------------
# Example root endpoint
# --------------------------
@app.get("/")
async def root():
    return {"message": "AI Car Customer Service API is running."}


app.include_router(api_router, prefix="/api/v1")

# --------------------------
# Run using python -m
# --------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
