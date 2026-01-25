import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import TicketsPerDayChart from "@/components/dashboard/tickets-per-day-chart";
import { getTicketsPerDay, getTicketsByPriority } from "@/lib/api";
import TicketPriorityPieChart from "@/components/dashboard/ticket-priority-pie-chart";


export default async function DashboardPage() {
  const  perDay = await getTicketsPerDay();
  const byPriority = await getTicketsByPriority()

  return (
    <div className="space-y-6">
      <h1 className="text-2xl font-bold">Dashboard</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Tickets per Day</CardTitle>
          </CardHeader>
          <CardContent>
            <TicketsPerDayChart data={perDay} />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Ticket Priority</CardTitle>
          </CardHeader>
          <CardContent>
            <TicketPriorityPieChart data={byPriority} />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}