content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

old = 'body: JSON.stringify({ mensaje: pregunta })'
new = 'body: JSON.stringify({ pregunta: pregunta, usuario_id: "web_user" })'

content = content.replace(old, new)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Campo corregido")