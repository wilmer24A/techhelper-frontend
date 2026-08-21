"use client"
import { useState } from "react"

const API_URL = "http://localhost:8002"
const TOKEN = "user_3I59hLkVRqSndxMj9KVIpYnwhDw"

export default function ChatPage() {
  const [mensajes, setMensajes] = useState([])
  const [input, setInput] = useState("")
  const [cargando, setCargando] = useState(false)

  async function enviar() {
    if (!input.trim() || cargando) return
    const pregunta = input.trim()
    setInput("")
    setMensajes(prev => [...prev, { role: "user", contenido: pregunta }])
    setCargando(true)
    try {
      const res = await fetch(API_URL + "/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": "Bearer " + TOKEN },
        body: JSON.stringify({ mensaje: pregunta })
      })
      const data = await res.json()
      setMensajes(prev => [...prev, { role: "agent", contenido: data.respuesta, categoria: data.categoria }])
    } catch {
      setMensajes(prev => [...prev, { role: "agent", contenido: "Error al conectar con el agente." }])
    }
    setCargando(false)
  }

  return (
    <div style={{minHeight:"100vh",background:"#f8f9fa",display:"flex",flexDirection:"column"}}>
      <header style={{background:"white",borderBottom:"1px solid #e5e7eb",padding:"16px 24px",display:"flex",justifyContent:"space-between",alignItems:"center"}}>
        <div>
          <h1 style={{fontSize:"18px",fontWeight:600,margin:0}}>TechHelper AI</h1>
          <p style={{fontSize:"13px",color:"#6b7280",margin:0}}>Soporte tecnico inteligente</p>
        </div>
        <a href="/" style={{fontSize:"13px",color:"#6b7280"}}>Inicio</a>
      </header>
      <div style={{flex:1,overflowY:"auto",padding:"24px",maxWidth:"760px",width:"100%",margin:"0 auto"}}>
        {mensajes.length === 0 && (
          <div style={{textAlign:"center",color:"#9ca3af",marginTop:"80px"}}>
            <p style={{fontSize:"18px"}}>En que puedo ayudarte?</p>
            <p style={{fontSize:"13px",marginTop:"8px"}}>Preguntame sobre instalacion, planes o integraciones</p>
          </div>
        )}
        {mensajes.map((m, i) => (
          <div key={i} style={{marginBottom:"16px",display:"flex",justifyContent:m.role==="user"?"flex-end":"flex-start"}}>
            <div style={{maxWidth:"80%",padding:"12px 16px",borderRadius:"12px",fontSize:"14px",lineHeight:1.6,background:m.role==="user"?"#111":"white",color:m.role==="user"?"white":"#1a1a1a",border:m.role==="user"?"none":"1px solid #e5e7eb"}}>
              {m.contenido}
              {m.categoria && <span style={{display:"block",fontSize:"11px",opacity:0.5,marginTop:"4px"}}>{m.categoria}</span>}
            </div>
          </div>
        ))}
        {cargando && (
          <div style={{display:"flex",justifyContent:"flex-start",marginBottom:"16px"}}>
            <div style={{background:"white",border:"1px solid #e5e7eb",padding:"12px 16px",borderRadius:"12px"}}>
              <span style={{color:"#9ca3af",fontSize:"13px"}}>Escribiendo...</span>
            </div>
          </div>
        )}
      </div>
      <div style={{background:"white",borderTop:"1px solid #e5e7eb",padding:"16px 24px"}}>
        <div style={{maxWidth:"760px",margin:"0 auto",display:"flex",gap:"12px"}}>
          <input
            type="text"
            value={input}
            onChange={e => setInput(e.target.value)}
            onKeyDown={e => e.key==="Enter" && enviar()}
            placeholder="Escribe tu pregunta..."
            style={{flex:1,border:"1px solid #e5e7eb",borderRadius:"8px",padding:"10px 14px",fontSize:"14px",outline:"none"}}
          />
          <button
            onClick={enviar}
            disabled={cargando}
            style={{background:"#111",color:"white",border:"none",borderRadius:"8px",padding:"10px 20px",fontSize:"14px",cursor:"pointer"}}
          >
            Enviar
          </button>
        </div>
      </div>
    </div>
  )
}