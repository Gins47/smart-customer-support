from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.services.ticket_service import TicketService
from app.types.ticket_update import TicketUpdateRequest

router = APIRouter(prefix="/tickets",tags=["tickets"])

@router.get("/")
async def list_tickets(db:AsyncSession = Depends(get_db)):
    try:
        service = TicketService()
        return await service.list_tickets(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/{ticket_id}")
async def get_ticket_by_id(ticket_id:int,db:AsyncSession = Depends(get_db)):
    try:
        service = TicketService()
        ticket = await service.get_ticket_by_id(db,ticket_id)
        if not ticket:
            raise HTTPException(status_code=404,detail="Ticket not found")
        return ticket

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    
@router.put("/{ticket_id}")
async def update_draft_ticket(ticket_id:int,payload:TicketUpdateRequest, db:AsyncSession = Depends(get_db)):
    try:
        service = TicketService()
        ticket = await service.update_draft_ticket(db,ticket_id,payload)
        if not ticket:
            raise HTTPException(status_code=404,detail="Ticket not found")
        return ticket

    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))