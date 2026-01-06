from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.api.deps import get_db
from app.integrations.email import EmailFetcher

router = APIRouter(prefix="/emails",tags=["emails"])

@router.post("/fetch_mail")
async def fetch_emails(db:AsyncSession = Depends(get_db)):
    try:
        emails = EmailFetcher()
        return await emails.fetchUserEmail(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
