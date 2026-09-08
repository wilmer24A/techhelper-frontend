content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

old = 'const res = await fetch(API_URL + "/chat", {'
new = 'const res = await fetch(API_URL + "/agente", {'

# También corrige el campo de respuesta
old2 = 'contenido: data.respuesta,'
new2 = 'contenido: data.respuesta || data.respuesta,'

content = content.replace(old, new)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Endpoint corregido")