from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ticket_repository import TicketRepository
from app.models.ticket import Ticket
from app.types.ticket import TicketUpdateRequest
from app.integrations.email import EmailHandler

class TicketService:

    def __init__(self):
        self.repo = TicketRepository()
        self.email_handler = EmailHandler()

    async def bulk_create_ticket(self,db:AsyncSession, ticket_list: list):
        ticket_creation_list = []
        for ticket in ticket_list:

            print(f"ticket for db = {ticket}")
            ticket_creation_list.append(
                    Ticket(
                            from_email=ticket["from_email"],
                            ticket_number=ticket["ticket_number"],
                            priority=ticket["priority"],
                            summary=ticket["summary"],
                            subject=ticket["subject"],
                            draft_response=ticket["draft_response"],
                            status='PENDING_REVIEW'
                        )
                    )
            await self.repo.bulk_create(db,ticket_creation_list)
    
    async def list_tickets(self,db:AsyncSession):
        return await self.repo.get_all(db)
    
    async def get_ticket_by_id(self,db:AsyncSession,ticket_id):
        return await self.repo.get_ticket_by_id(db,ticket_id)
    
    async def update_draft_ticket(self,db:AsyncSession,ticket_id,payload:TicketUpdateRequest):
        result = await self.repo.update_draft_ticket(db,ticket_id,payload)
        print(f"Ticket Approved {result}")
        if result and result.status == "APPROVED":
            self.email_handler.send_email(
                result.from_email,
                "RE: "+result.ticket_number + " - "+result.subject,
                result.draft_response
            )
            
        return result
    
    async def get_tickets_per_day(self,db:AsyncSession):
        return await self.repo.get_tickets_per_day(db)

    async def get_tickets_by_status(self,db:AsyncSession):
        return await self.repo.get_tickets_by_status(db)

    async def get_tickets_by_priority(self,db:AsyncSession):
        return await self.repo.get_tickets_by_priority(db)
