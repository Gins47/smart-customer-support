import { Ticket } from "@/types/ticket";

const API_BASE_URL =
  process.env.NEXT_PUBLIC_API_BASE_URL || "http://localhost:8000";

export async function fetchTickets(): Promise<Ticket[]> {
  const res = await fetch(`${API_BASE_URL}/api/v1/tickets`, {
    cache: "no-store", // always fresh data
  });

  if (!res.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return res.json();
}

export async function fetchTicketById(ticket_id: string): Promise<Ticket> {
  const res = await fetch(`${API_BASE_URL}/api/v1/tickets/${ticket_id}`, {
    cache: "no-cache",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch ticket details");
  }

  return res.json();
}

export async function saveDraftEmail(
  ticket_id: number,
  draft_response: string
) {
  const res = await fetch(`${API_BASE_URL}/api/v1/tickets/${ticket_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ draft_response }),
  });

  if (!res.ok) {
    throw new Error("Failed to save draft ticket details");
  }

  return res.json();
}

export async function updateTicketStatus(ticket_id: number, status: string) {
  const res = await fetch(`${API_BASE_URL}/api/v1/tickets/${ticket_id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ status }),
  });

  if (!res.ok) {
    throw new Error("Update ticket status");
  }

  return res.json();
}

export async function getTicketsPerDay() {
  const res = await fetch(`${API_BASE_URL}/api/v1/analytics`, {
    cache: "no-store", // always fresh data
  });

  if (!res.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return res.json();
}

export async function getTicketsByPriority() {
  const res = await fetch(`${API_BASE_URL}/api/v1/analytics/priority`, {
    cache: "no-store", // always fresh data
  });

  if (!res.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return res.json();
}

export async function getTicketsByStatus() {
  const res = await fetch(`${API_BASE_URL}/api/v1/analytics/status`, {
    cache: "no-store", // always fresh data
  });

  if (!res.ok) {
    throw new Error("Failed to fetch tickets");
  }

  return res.json();
}
