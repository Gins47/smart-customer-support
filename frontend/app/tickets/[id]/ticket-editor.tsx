"use client"

import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"
import { saveDraftEmail } from "@/lib/api"
import { Ticket } from "@/types/ticket"
import { useState } from "react"

export default function TicketEditor({ticket}: {ticket:Ticket }) {
const [draft,setDraft] = useState(ticket.draft_response)
const [saving,setSaving] = useState(false)

async function saveDraft() {
    setSaving(true)
    await saveDraftEmail(ticket.id,draft)
    setSaving(false)
    alert("Draft Saved")
}

return (
    <div className="space-y-4">
        <Textarea value={draft} rows={10} onChange={(e)=>setDraft(e.target.value)} />
  
        <Button onClick={saveDraft} disabled={saving}>
        {saving ? "Saving...":"Save Draft"}
        </Button>
    </div>
)
}