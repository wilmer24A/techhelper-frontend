content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

old = 'const res = await fetch(API_URL + "/agente", {'
new = 'const res = await fetch(API_URL + "/chat", {'

content = content.replace(old, new)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Endpoint corregido")