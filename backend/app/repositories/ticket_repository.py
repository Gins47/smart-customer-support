from sqlalchemy.ext.asyncio import AsyncSession
from app.models.ticket import Ticket
from sqlalchemy import select, update, func

from app.types.ticket_update import TicketUpdateRequest


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
    
    async def get_ticket_by_id(self, db:AsyncSession, ticket_id:int) -> Ticket | None:
        query = select(Ticket).where(Ticket.id == ticket_id)
        result = await db.execute(query)
        return result.scalar_one_or_none()
    
    async def update_draft_ticket(self, db:AsyncSession, ticket_id:int, payload:TicketUpdateRequest) -> Ticket | None:
        values = payload.model_dump(exclude_unset=True)

        if not values:
            return None
        
        query = (update(Ticket).where(Ticket.id == ticket_id).values(**values).returning(Ticket))
        result = await db.execute(query)
        await db.commit()
        return result.scalar_one_or_none()
    
    async def update_status(self,db:AsyncSession,ticket_id:int,new_status:str) -> Ticket | None:
        query = update(Ticket).where(Ticket.id == ticket_id).values(status= new_status)
        result = await db.execute(query)
        await db.commit()
        return result.scalar_one_or_none()
    
    async def get_tickets_per_day(self,db:AsyncSession):
        query = (
                 select(func.date(Ticket.created_at).label('date'),
                        func.count(Ticket.id).label('count')
                     )
                    .group_by(func.date(Ticket.created_at))
                    .order_by(func.date(Ticket.created_at))
                )
        result = await db.execute(query)
        return result.mappings().all()