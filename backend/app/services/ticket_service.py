from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ticket_repository import TicketRepository
from app.models.ticket import Ticket
from app.types.ticket_update import TicketUpdateRequest

class TicketService:

    def __init__(self):
        self.repo = TicketRepository()

    async def create_ticket(self,db:AsyncSession, ticket_list: list):
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
        return await self.repo.update_draft_ticket(db,ticket_id,payload)
    

    async def get_tickets_per_day(self,db:AsyncSession):
        return await self.repo.get_tickets_per_day(db)

    async def get_tickets_by_status(self,db:AsyncSession):
        return await self.repo.get_tickets_by_status(db)

    async def get_tickets_by_priority(self,db:AsyncSession):
        return await self.repo.get_tickets_by_priority(db)
