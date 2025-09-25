export default function DashboardPage() {
  return (
    <div className="min-h-screen bg-gray-50">
      <div className="py-10">
        <header>
          <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold leading-tight text-gray-900">Dashboard</h1>
          </div>
        </header>
        <main>
          <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
            <div className="px-4 py-8 sm:px-0">
              <div className="border-4 border-dashed border-gray-200 rounded-lg h-96 p-8">
                <h2 className="text-xl font-semibold mb-4">Welcome to DocSync</h2>
                <p className="text-gray-600 mb-6">Manage your documentation integrations and sync jobs.</p>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                  <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-lg font-medium mb-2">Integrations</h3>
                    <p className="text-gray-600">Connect your platforms</p>
                    <a href="/dashboard/integrations" className="text-indigo-600 hover:text-indigo-500 mt-2 inline-block">
                      Manage →
                    </a>
                  </div>
                  <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-lg font-medium mb-2">Documents</h3>
                    <p className="text-gray-600">View synced documents</p>
                    <a href="/dashboard/documents" className="text-indigo-600 hover:text-indigo-500 mt-2 inline-block">
                      Browse →
                    </a>
                  </div>
                  <div className="bg-white p-6 rounded-lg shadow">
                    <h3 className="text-lg font-medium mb-2">Sync Jobs</h3>
                    <p className="text-gray-600">Monitor sync status</p>
                    <a href="/dashboard/sync-jobs" className="text-indigo-600 hover:text-indigo-500 mt-2 inline-block">
                      View →
                    </a>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}
