"use client"
import { useState } from "react"

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8002"
const TOKEN = process.env.NEXT_PUBLIC_TOKEN || "user_3I59hLkVRqSndxMj9KVIpYnwhDw"

export default function ChatPage() {
  const [mensajes, setMensajes] = useState<{role:string,contenido:string,categoria:string}[]>([])
  const [input, setInput] = useState("")
  const [cargando, setCargando] = useState(false)

  async function enviar() {
    if (!input.trim() || cargando) return
    const pregunta = input.trim()
    setInput("")
    setMensajes(prev => [...prev, { role: "user", contenido: pregunta, categoria: "" }])
    setCargando(true)

    setMensajes(prev => [...prev, { role: "agent", contenido: "", categoria: "" }])

    try {
      const res = await fetch(API_URL + "/chat/stream", {
        method: "POST",
        headers: { "Content-Type": "application/json", "Authorization": "Bearer " + TOKEN },
        body: JSON.stringify({ mensaje: pregunta })
      })

      if (!res.body) return
      const reader = res.body.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        const lines = chunk.split("\n")

        for (const line of lines) {
          if (!line.startsWith("data: ")) continue
          try {
            const data = JSON.parse(line.slice(6))
            if (data.token) {
              setMensajes(prev => {
                const nuevo = [...prev]
                nuevo[nuevo.length - 1] = {
                  ...nuevo[nuevo.length - 1],
                  contenido: nuevo[nuevo.length - 1].contenido + data.token
                }
                return nuevo
              })
            }
            if (data.done) {
              setMensajes(prev => {
                const nuevo = [...prev]
                nuevo[nuevo.length - 1] = {
                  ...nuevo[nuevo.length - 1],
                  categoria: data.categoria
                }
                return nuevo
              })
            }
          } catch {}
        }
      }
    } catch {
      setMensajes(prev => {
        const nuevo = [...prev]
        nuevo[nuevo.length - 1] = { role: "agent", contenido: "Error al conectar con el agente.", categoria: "" }
        return nuevo
      })
    }
    setCargando(false)
  }

  return (
    <div style={{minHeight:"calc(100vh - 56px)",background:"#f8f9fa",display:"flex",flexDirection:"column"}}>
      <div style={{flex:1,overflowY:"auto",padding:"24px",maxWidth:"760px",width:"100%",margin:"0 auto"}}>
        {mensajes.length === 0 && (
          <div style={{textAlign:"center",color:"#9ca3af",marginTop:"80px"}}>
            <p style={{fontSize:"18px"}}>En que puedo ayudarte?</p>
            <p style={{fontSize:"13px",marginTop:"8px"}}>Preguntame sobre instalacion, planes o integraciones</p>
          </div>
        )}
        {mensajes.map((m, i) => (
          <div key={i} style={{marginBottom:"16px",display:"flex",justifyContent:m.role==="user"?"flex-end":"flex-start"}}>
            <div style={{maxWidth:"80%",padding:"12px 16px",borderRadius:"12px",fontSize:"14px",lineHeight:1.6,background:m.role==="user"?"#111":"white",color:m.role==="user"?"white":"#1a1a1a",border:m.role==="user"?"none":"1px solid #e5e7eb",whiteSpace:"pre-wrap"}}>
              {m.contenido}
              {m.contenido === "" && m.role === "agent" && <span style={{color:"#9ca3af"}}>▍</span>}
              {m.categoria && <span style={{display:"block",fontSize:"11px",opacity:0.5,marginTop:"4px"}}>{m.categoria}</span>}
            </div>
          </div>
        ))}
      </div>
      <div style={{background:"white",borderTop:"1px solid #e5e7eb",padding:"16px 24px",position:"sticky",bottom:0}}>
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
            style={{background:"#111",color:"white",border:"none",borderRadius:"8px",padding:"10px 20px",fontSize:"14px",cursor:"pointer",opacity:cargando?0.5:1}}
          >
            {cargando ? "..." : "Enviar"}
          </button>
        </div>
      </div>
    </div>
  )
}