import { Card, CardContent } from "@/components/ui/card"

type KPICardProps = {
  title: string
  value: number
  icon?: React.ReactNode
}

export function KPICard({ title, value, icon }: KPICardProps) {
  return (
    <Card className="relative overflow-hidden">
    <CardContent className="p-6">
        <div className="flex items-center gap-4">
        {/* Icon */}
        <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/10 text-primary text-2xl">
            {icon}
        </div>

        {/* Value + Title */}
        <div>
            <p className="text-sm text-muted-foreground mt-1">
            {title}
            </p>
            <p className="text-5xl font-extrabold leading-none">
            {value}
            </p>
        </div>
        </div>
    </CardContent>
    </Card>
  )
}
