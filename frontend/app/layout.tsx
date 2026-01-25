import "./globals.css";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen bg-gray-100">
        <div className="flex h-screen">
          {/* Sidebar */}
          <aside className="w-64 bg-slate-900 text-white p-4">
            <h2 className="text-xl font-bold mb-6">🚗 Car Support</h2>

            <nav className="space-y-2">
              <a
                href="/tickets"
                className="block rounded px-3 py-2 hover:bg-slate-800"
              >
                🎫 Tickets
              </a>
            </nav>
          </aside>

          {/* Main Content */}
          <div className="flex-1 flex flex-col">
            {/* Header */}
            <header className="h-14 bg-white border-b px-6 flex items-center">
              <h1 className="font-semibold">Admin Dashboard</h1>
            </header>

            {/* Page Content */}
            <main className="flex-1 overflow-y-auto p-6">
              {children}
            </main>
          </div>
        </div>
      </body>
    </html>
  );
}
