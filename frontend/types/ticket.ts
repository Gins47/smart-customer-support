export interface Ticket {
  id: number;
  ticket_number: string;
  priority: "LOW" | "MEDIUM" | "HIGH" | "CRITICAL";
  status: string;
  subject: string;
  summary: string;
  from_email: string;
  draft_response: string;
  created_at: string;
}
