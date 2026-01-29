# 🚗 AI Car Customer Support – Multi Agent Ticketing System Using OpenAI Agents SDK

AI powered customer support system that converts incoming emails into support tickets. The system generates draft responses using AI agents using available tools and the human agents review, edit, approve or reject the AI generated responses via a web application before sending it to the customers.

# ✨ Features

- 📩 Email ingestion (Gmail)
- 🤖 AI agent analyze emails and generates
  - Priority
  - Summary
  - Draft response
- 🧑‍💼 Human-in-the-loop approval before sending response to users
  - ✏️ Editable draft responses
  - ✅ Approve / ❌ Reject tickets
- 📊 Analytics dashboard
  - Tickets per day
  - Tickets by priority
  - Tickets by status
  - Total tickets & pending review

# Architecture Overview

![Architecture Diagram](./images/architecture_diagram.png)

# 🚀 Technologies

- **PostgreSQL** – Data storage
- **FastAPI** – Backend API implementation
- **LLM (GPT-5 Nano)** – Language model powering the AI agent
- **Next.js** – Frontend web application
- **Docker Compose** – Service orchestration

# ⚙️ Setup

## Environment Variables

- backend (backend/.env)

```shell
EMAIL_USER=""
EMAIL_PASSWORD=""
OPENAI_API_KEY=sk-proj-
DATABASE_URL="postgresql+asyncpg://appuser:apppassword@localhost:5432/carsupport"
```

## Build & start services

```shell
docker compose build --no-cache
docker compose up -d
```

**Access application**

- Frontend: **http://localhost:3000**
- Backend: **http://localhost:8000**
- API Docs: **http://localhost:8000/docs**

# 🚀 Future Improvements

- Authentication & roles
- LLM provider switching
- More KPIs
- UI Improvements
