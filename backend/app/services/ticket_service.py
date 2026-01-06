from sqlalchemy.ext.asyncio import AsyncSession
from app.repositories.ticket_repository import TicketRepository
from app.models.ticket import Ticket

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
    

