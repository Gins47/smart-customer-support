from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.services.ticket_service import TicketService

router = APIRouter(prefix="/tickets",tags=["tickets"])

@router.get("/")
async def list_tickets(db:AsyncSession = Depends(get_db)):
    try:
        service = TicketService()
        return await service.list_tickets(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))