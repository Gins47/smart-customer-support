from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.integrations.email import EmailHandler
from app.services.ticket_service import TicketService
from app.types.ticket import TicketCreateRequest

router = APIRouter(prefix="/emails",tags=["emails"])

@router.post("/fetch_mail")
async def fetch_emails(db:AsyncSession = Depends(get_db)):
    try:
        emails = EmailHandler()
        ticket_service = TicketService()
        response = await emails.fetchUserEmail()
        return await ticket_service.bulk_create_ticket(db,response)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.post("/")
async def create_email(payload:TicketCreateRequest,db:AsyncSession = Depends(get_db),):
    try:
        print(f"payload = {payload}")
        emails = EmailHandler()
        ticket_service = TicketService()
        response = await emails.process_email(payload)
        return await ticket_service.bulk_create_ticket(db,response)
    
    except Exception as e:
        print(f"Error occurent in POSR /email = {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

