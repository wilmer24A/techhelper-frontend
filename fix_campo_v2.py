content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

old = 'body: JSON.stringify({ pregunta: pregunta, usuario_id: "web_user" })'
new = 'body: JSON.stringify({ mensaje: pregunta })'

content = content.replace(old, new)

# También actualiza el campo de respuesta
old2 = 'contenido: data.respuesta || data.respuesta,'
new2 = 'contenido: data.respuesta,'

content = content.replace(old2, new2)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Campo actualizado")