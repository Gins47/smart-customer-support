import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import TicketsPerDayChart from "@/components/dashboard/tickets-per-day-chart";
import { getTicketsPerDay, getTicketsByPriority, getTicketsByStatus } from "@/lib/api";
import TicketPriorityPieChart from "@/components/dashboard/ticket-priority-pie-chart";
import TicketStatusPieChart from "@/components/dashboard/ticket-status-pie-chart";
import { KPICard } from "@/components/dashboard/kpi-card";

type TicketStatusCount = {
  status:string
  count:number
}

function getTicketKpis(stats:TicketStatusCount[]) {
  const totalTickets = stats.reduce(( sum, stat ) => sum + stat.count, 0 )
  const pendingReview = stats.find((stats) => stats.status === 'PENDING_REVIEW')?.count ?? 0
  return { totalTickets, pendingReview}
}

export default async function DashboardPage() {
  const ticketsPerDay = await getTicketsPerDay();
  const ticketsByPriority = await getTicketsByPriority()
  const ticketsByStatus = await getTicketsByStatus()
  const ticketKpis = getTicketKpis(ticketsByStatus)

  return (
    <div className="space-y-6">

    <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
      <KPICard
        title="Total Tickets"
        value={ticketKpis.totalTickets}
        icon={<span>📧</span>}
      />
      <KPICard
        title="Pending Review"
        value={ticketKpis.pendingReview}
        icon={<span>⏳</span>}
      />
    </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <Card className="md:col-span-2">
          <CardHeader>
            <CardTitle>Tickets per Day</CardTitle>
          </CardHeader>
          <CardContent>
            <TicketsPerDayChart data={ticketsPerDay} />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Ticket Priority</CardTitle>
          </CardHeader>
          <CardContent>
            <TicketPriorityPieChart data={ticketsByPriority} />
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Ticket Status</CardTitle>
          </CardHeader>
          <CardContent>
            <TicketStatusPieChart data={ticketsByStatus} />
          </CardContent>
        </Card>
      </div>
    </div>
  );
}