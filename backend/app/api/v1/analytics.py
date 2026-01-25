from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.services.ticket_service import TicketService
from app.types.ticket_update import TicketUpdateRequest

router = APIRouter(prefix="/analytics",tags=["analytics"])

@router.get("/")
async def ticketsPerDay(db:AsyncSession = Depends(get_db)):
    try:
        service = TicketService()
        return await service.get_tickets_per_day(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))