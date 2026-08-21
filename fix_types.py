# Fix chat/page.tsx - añade tipos TypeScript
chat = open('app/chat/page.tsx', 'r', encoding='utf-8').read()
chat = chat.replace(
    'const [mensajes, setMensajes] = useState([])',
    'const [mensajes, setMensajes] = useState<{role:string,contenido:string,categoria:string}[]>([])'
)
chat = chat.replace(
    "const [perfil, setPerfil] = useState(null)",
    "const [perfil, setPerfil] = useState<any>(null)"
)
chat = chat.replace(
    "if (res.body) {",
    ""
)

# Fix res.body possibly null
chat = chat.replace(
    "      const reader = res.body.getReader()",
    "      if (!res.body) return\n      const reader = res.body.getReader()"
)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(chat)

# Fix perfil/page.tsx - añade tipos TypeScript  
perfil = open('app/perfil/page.tsx', 'r', encoding='utf-8').read()
perfil = perfil.replace(
    'const [perfil, setPerfil] = useState(null)',
    'const [perfil, setPerfil] = useState<any>(null)'
)
perfil = perfil.replace(
    'const [conversaciones, setConversaciones] = useState([])',
    'const [conversaciones, setConversaciones] = useState<any[]>([])'
)

with open('app/perfil/page.tsx', 'w', encoding='utf-8') as f:
    f.write(perfil)

print("Tipos corregidos correctamente")