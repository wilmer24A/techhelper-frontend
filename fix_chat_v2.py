content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

# Busca y reemplaza la línea problemática
old = '{ role: "user", contenido: pregunta }'
new = '{ role: "user", contenido: pregunta, categoria: "" }'

content = content.replace(old, new)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

# Verifica
result = open('app/chat/page.tsx', 'r', encoding='utf-8').read()
if '{ role: "user", contenido: pregunta, categoria: "" }' in result:
    print("Fix aplicado correctamente")
else:
    print("ERROR: Fix no se aplicó")