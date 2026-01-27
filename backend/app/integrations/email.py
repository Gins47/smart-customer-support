import os
from typing import List, Dict
from imap_tools import AND, MailBox
import smtplib
from email.message import EmailMessage
from sqlalchemy.ext.asyncio import AsyncSession
from app.agents.orchestrator import run_orchestrator_agent
from app.core.config import settings
from app.services.ticket_service import TicketService


class EmailFetcher:
    def __init__(self):
        self.server = "imap.gmail.com"
        self.user = settings.EMAIL_USER
        self.password = settings.EMAIL_PASSWORD
        self.ticket_service = TicketService()

        if not self.user or not self.password:
            raise RuntimeError("EMAIL_USER or PASSWORD is not set")

    async def fetchUserEmail(self, db:AsyncSession, limit=10):
        """
        Fetches unread email from Gmail account

        """
        response = []
        print(f"user = {self.user} , password = {self.password}")
        with MailBox(self.server).login(username=self.user,password=self.password) as mailBox:
            print(f" Connected to gmail of {self.user}")

            mail_list = mailBox.fetch(criteria=AND(seen=False),limit=limit,mark_seen=False)
            
            for msg in mail_list:
                print(f"From: {msg.from_}  |  Subject: {msg.subject} text = {msg.text}")
                agent_output = await run_orchestrator_agent(msg.text or "")
                print(f" agent response = {agent_output}")
                response.append({
                    "from_email": msg.from_,
                    "subject": msg.subject,
                    "priority": agent_output.priority,
                    "summary": agent_output.summary,
                    "ticket_number": agent_output.ticket_number,
                    "draft_response": agent_output.draft_response,
                })

        print(f"Saving tickets to database = {response}")
        return await self.ticket_service.create_ticket(db,response)

class EmailSender:
    def __init__(self):
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.user = settings.EMAIL_USER
        self.password = settings.EMAIL_PASSWORD

        if not self.user or not self.password:
            raise RuntimeError("EMAIL_USER or EMAIL_PASSWORD is not set")

    def send_email(
        self,
        to_email: str,
        subject: str,
        body: str,
    ) -> None:
        msg = EmailMessage()
        msg["From"] = self.user
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.user, self.password)
            server.send_message(msg)