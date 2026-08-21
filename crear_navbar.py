import os
os.makedirs('app/components', exist_ok=True)

navbar = '''"use client"
import { usePathname } from "next/navigation"

export default function Navbar() {
  const pathname = usePathname()

  const links = [
    { href: "/", label: "Inicio" },
    { href: "/chat", label: "Chat" },
    { href: "/perfil", label: "Mi Perfil" },
  ]

  return (
    <nav style={{background:"white",borderBottom:"1px solid #e5e7eb",padding:"0 24px",display:"flex",alignItems:"center",justifyContent:"space-between",height:"56px",position:"sticky",top:0,zIndex:100}}>
      <div style={{display:"flex",alignItems:"center",gap:"8px"}}>
        <div style={{width:"28px",height:"28px",background:"#111",borderRadius:"6px",display:"flex",alignItems:"center",justifyContent:"center"}}>
          <span style={{color:"white",fontSize:"14px",fontWeight:700}}>T</span>
        </div>
        <span style={{fontSize:"15px",fontWeight:600,color:"#111"}}>TechHelper AI</span>
      </div>
      <div style={{display:"flex",gap:"4px"}}>
        {links.map(link => (
          
            key={link.href}
            href={link.href}
            style={{
              padding:"6px 14px",
              borderRadius:"6px",
              fontSize:"13px",
              fontWeight:500,
              color: pathname === link.href ? "#111" : "#6b7280",
              background: pathname === link.href ? "#f3f4f6" : "transparent",
              textDecoration:"none",
            }}
          >
            {link.label}
          </a>
        ))}
      </div>
    </nav>
  )
}'''

layout = '''import type { Metadata } from "next"
import "./globals.css"
import Navbar from "./components/Navbar"

export const metadata: Metadata = {
  title: "TechHelper AI",
  description: "Soporte tecnico con inteligencia artificial",
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body style={{margin:0,fontFamily:"-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif"}}>
        <Navbar />
        {children}
      </body>
    </html>
  )
}'''

with open('app/components/Navbar.tsx', 'w', encoding='utf-8') as f:
    f.write(navbar)

with open('app/layout.tsx', 'w', encoding='utf-8') as f:
    f.write(layout)

print("Navbar y layout actualizados correctamente")