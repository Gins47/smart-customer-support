from sqlalchemy.ext.asyncio import AsyncSession
from app.models.ticket import Ticket
from sqlalchemy import select


class TicketRepository:
    async def create(self, db:AsyncSession, ticket:Ticket):
        db.add(ticket)
        await db.commit()
        await db.refresh(ticket)
        return ticket
    
    async def bulk_create(self, db:AsyncSession, ticket_list:list):
        db.add_all(ticket_list)
        return await db.commit()
         

    
    async def get_all(self, db:AsyncSession):
        result = await db.execute(select(Ticket))
        return result.scalars().all()