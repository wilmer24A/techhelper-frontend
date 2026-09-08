content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

old = 'const res = await fetch(API_URL + "/chat/stream", {'
new = 'const res = await fetch(API_URL + "/chat", {'

content = content.replace(old, new)

# Simplifica el procesamiento de respuesta
old2 = '''      const reader = res.body.getReader()
      const decoder = new TextDecoder()

      while (true) {
        const { done, value } = await reader.read()
        if (done) break

        const chunk = decoder.decode(value)
        const lines = chunk.split("\\n")

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
      }'''

new2 = '''      const data = await res.json()
      setMensajes(prev => {
        const nuevo = [...prev]
        nuevo[nuevo.length - 1] = {
          role: "agent",
          contenido: data.respuesta,
          categoria: data.categoria || ""
        }
        return nuevo
      })'''

content = content.replace(old2, new2)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Chat actualizado sin streaming")