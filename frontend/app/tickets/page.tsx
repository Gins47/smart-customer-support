import { Card } from "@/components/ui/card";
import Link from "next/link";
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Badge } from "@/components/ui/badge";
import { fetchTickets } from "@/lib/api";
import TicketActions from "./tickets-action";

type Ticket = {
  id: number;
  ticket_number: string;
  subject: string;
  priority: string;
  status: string;
  from_email: string;
  created_at: string;
};

export default async function TicketsPage() {
  const tickets = await fetchTickets();
  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Tickets</h1>

      <div className="rounded-lg border">
        <Table>
          <TableHeader>
            <TableRow>
              <TableHead>Ticket #</TableHead>
              <TableHead>Subject</TableHead>
              <TableHead>Priority</TableHead>
              <TableHead>Status</TableHead>
              <TableHead>Actions</TableHead>
            </TableRow>
          </TableHeader>

          <TableBody>
            {tickets.map((ticket) => (
              <TableRow
                key={ticket.id}
              >
                <TableCell><Link href={`/tickets/${ticket.id}`} className="text-blue-600 hover:underline">{ticket.ticket_number}</Link></TableCell>
                <TableCell>{ticket.subject}</TableCell>
                <TableCell>
                  <Badge>{ticket.priority}</Badge>
                </TableCell>
                <TableCell>
                  <Badge variant="outline">{ticket.status}</Badge>
                </TableCell>

              <TableCell>
                {ticket.status === "PENDING_REVIEW" && (
                  <TicketActions ticketId={ticket.id} />
                )}
              </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </div>
    </div>
  );
}
