from fastapi import APIRouter
from app.api.v1 import tickets, email, analytics

api_router = APIRouter()

api_router.include_router(tickets.router)
api_router.include_router(email.router)
api_router.include_router(analytics.router)
