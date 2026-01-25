"use client";

import { Button } from "@/components/ui/button";
import { updateTicketStatus } from "@/lib/api";
import { Check, X } from "lucide-react";
import { useRouter } from "next/navigation";

type Props = {
  ticketId: number;
};

export default function TicketActions({ ticketId }: Props) {
  const router = useRouter();

  async function updateStatus(status: "APPROVED" | "REJECTED") {
    await updateTicketStatus(ticketId,status)

    // Refresh ticket list
    router.refresh();
  }

  return (
    <div className="flex gap-2">
      <Button
        size="sm"
        className="bg-green-600 hover:bg-green-700 text-white"
        onClick={() => updateStatus("APPROVED")}
      >
         <Check className="h-4 w-4" />
      </Button>

      <Button
        size="sm"
        variant="destructive"
        onClick={() => updateStatus("REJECTED")}
      >
        <X size={16} />
      </Button>
    </div>
  );
}
