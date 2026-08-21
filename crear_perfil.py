import os
os.makedirs('app/perfil', exist_ok=True)

content = '''"use client"
import { useState, useEffect } from "react"

const API_URL = "http://localhost:8002"
const TOKEN = "user_3I59hLkVRqSndxMj9KVIpYnwhDw"

export default function PerfilPage() {
  const [perfil, setPerfil] = useState(null)
  const [conversaciones, setConversaciones] = useState([])
  const [cargando, setCargando] = useState(true)

  useEffect(() => {
    async function cargarDatos() {
      try {
        const headers = { "Authorization": "Bearer " + TOKEN }

        const [resPerfil, resConv] = await Promise.all([
          fetch(API_URL + "/mi-perfil", { headers }),
          fetch(API_URL + "/mis-conversaciones", { headers })
        ])

        const dataPerfil = await resPerfil.json()
        const dataConv = await resConv.json()

        setPerfil(dataPerfil)
        setConversaciones(dataConv.conversaciones || [])
      } catch (e) {
        console.error("Error cargando perfil:", e)
      }
      setCargando(false)
    }
    cargarDatos()
  }, [])

  if (cargando) {
    return (
      <div style={{minHeight:"100vh",display:"flex",alignItems:"center",justifyContent:"center",background:"#f8f9fa"}}>
        <p style={{color:"#9ca3af"}}>Cargando perfil...</p>
      </div>
    )
  }

  return (
    <div style={{minHeight:"100vh",background:"#f8f9fa"}}>
      <header style={{background:"white",borderBottom:"1px solid #e5e7eb",padding:"16px 24px",display:"flex",justifyContent:"space-between",alignItems:"center"}}>
        <h1 style={{fontSize:"18px",fontWeight:600,margin:0}}>Mi Perfil</h1>
        <div style={{display:"flex",gap:"16px"}}>
          <a href="/chat" style={{fontSize:"13px",color:"#6b7280"}}>Chat</a>
          <a href="/" style={{fontSize:"13px",color:"#6b7280"}}>Inicio</a>
        </div>
      </header>

      <div style={{maxWidth:"760px",margin:"0 auto",padding:"32px 24px"}}>
        {perfil && (
          <div style={{background:"white",borderRadius:"12px",border:"1px solid #e5e7eb",padding:"24px",marginBottom:"24px"}}>
            <h2 style={{fontSize:"16px",fontWeight:600,marginBottom:"16px",color:"#111"}}>Información de cuenta</h2>
            <div style={{display:"grid",gap:"12px"}}>
              <div style={{display:"flex",justifyContent:"space-between",padding:"12px 0",borderBottom:"1px solid #f3f4f6"}}>
                <span style={{fontSize:"13px",color:"#6b7280"}}>Email</span>
                <span style={{fontSize:"13px",color:"#111",fontWeight:500}}>{perfil.email}</span>
              </div>
              <div style={{display:"flex",justifyContent:"space-between",padding:"12px 0",borderBottom:"1px solid #f3f4f6"}}>
                <span style={{fontSize:"13px",color:"#6b7280"}}>Plan</span>
                <span style={{fontSize:"13px",fontWeight:500,padding:"2px 10px",borderRadius:"20px",background:perfil.plan==="pro"?"#EAF3DE":"#f3f4f6",color:perfil.plan==="pro"?"#27500A":"#374151"}}>{perfil.plan}</span>
              </div>
              <div style={{display:"flex",justifyContent:"space-between",padding:"12px 0"}}>
                <span style={{fontSize:"13px",color:"#6b7280"}}>Hechos en memoria</span>
                <span style={{fontSize:"13px",color:"#111",fontWeight:500}}>{perfil.hechos_en_memoria}</span>
              </div>
            </div>
          </div>
        )}

        <div style={{background:"white",borderRadius:"12px",border:"1px solid #e5e7eb",padding:"24px"}}>
          <h2 style={{fontSize:"16px",fontWeight:600,marginBottom:"16px",color:"#111"}}>
            Historial de conversaciones ({conversaciones.length})
          </h2>
          {conversaciones.length === 0 ? (
            <p style={{fontSize:"13px",color:"#9ca3af",textAlign:"center",padding:"24px 0"}}>
              No tienes conversaciones todavía. Ve al chat para empezar.
            </p>
          ) : (
            <div style={{display:"grid",gap:"8px"}}>
              {conversaciones.map((conv, i) => (
                <div key={i} style={{display:"flex",justifyContent:"space-between",alignItems:"center",padding:"12px",borderRadius:"8px",background:"#f8f9fa"}}>
                  <div>
                    <p style={{fontSize:"13px",color:"#111",margin:0,fontWeight:500}}>
                      Conversación {conversaciones.length - i}
                    </p>
                    <p style={{fontSize:"11px",color:"#9ca3af",margin:"2px 0 0"}}>
                      {new Date(conv.timestamp).toLocaleDateString("es-ES", {
                        day:"numeric",month:"long",year:"numeric",hour:"2-digit",minute:"2-digit"
                      })}
                    </p>
                  </div>
                  <span style={{fontSize:"12px",color:"#6b7280",background:"white",border:"1px solid #e5e7eb",padding:"4px 10px",borderRadius:"20px"}}>
                    {conv.total_mensajes} mensajes
                  </span>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  )
}'''

with open('app/perfil/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Página de perfil creada correctamente")