from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from app.db.base import Base

class Ticket(Base):
   __tablename__ = "tickets"
   id = Column(Integer,primary_key=True)
   from_email = Column(String)
   ticket_number = Column(String,unique=True,index=True)
   priority = Column(String,index=True)
   subject = Column(String)
   summary = Column(String)
   draft_response = Column(Text)
   status = Column(String,default="PENDING_REVIEW")
   created_at = Column(DateTime(timezone=True), server_default=func.now())