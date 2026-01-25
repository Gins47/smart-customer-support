import { notFound } from "next/navigation";
import TicketEditor from "./ticket-editor";
import { fetchTicketById } from "@/lib/api";
import BackButton from "@/components/ui/back-button";
type Props = {
  params: Promise<{ id: string }>;
};

export default async function TicketDetailsPage({
  params,
}: Props) {

    const { id } = await params

    console.log(` params in tickets id page = ${id}`)
  const ticket = await fetchTicketById(id);

  if (!ticket) notFound();

  return (
    <div className="max-w-3xl space-y-6">
         {/* Back button */}
      <BackButton />

      <h1 className="text-2xl font-bold">{ticket.subject}</h1>

      <div className="text-sm text-muted-foreground">
        {ticket.ticket_number} · {ticket.priority}
      </div>

      <div className="text-sm">
        <span className="text-l font-bold">Summary :</span> {ticket.summary}
      </div>

      <TicketEditor ticket={ticket} />
    </div>
  );
}