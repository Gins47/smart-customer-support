from pydantic import BaseModel
from typing import Optional

class TicketUpdateRequest(BaseModel):
    draft_response:Optional[str] = None
    status:Optional[str] = None

class TicketCreateRequest(BaseModel):
    subject:str = None
    email:str = None
    from_email:str = None