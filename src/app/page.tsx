export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center">
      <div className="text-center">
        <h1 className="text-4xl font-semibold text-gray-900 mb-4">
          TechHelper AI
        </h1>
        <p className="text-gray-500 mb-8">
          Tu asistente de soporte técnico con inteligencia artificial
        </p>
        <div className="flex gap-4 justify-center">
          <a href="/chat" className="bg-black text-white px-6 py-3 rounded-lg font-medium">
            Ir al Chat
          </a>
          <a href="/perfil" className="border border-gray-300 text-gray-700 px-6 py-3 rounded-lg font-medium">
            Mi Perfil
          </a>
        </div>
      </div>
    </main>
  )
}