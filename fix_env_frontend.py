# Actualiza chat/page.tsx
chat_content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()
chat_content = chat_content.replace(
    'const API_URL = "http://localhost:8002"',
    'const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8002"'
)
chat_content = chat_content.replace(
    'const TOKEN = "user_3I59hLkVRqSndxMj9KVIpYnwhDw"',
    'const TOKEN = process.env.NEXT_PUBLIC_TOKEN || "user_3I59hLkVRqSndxMj9KVIpYnwhDw"'
)
with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(chat_content)

# Actualiza perfil/page.tsx
perfil_content = open('app/perfil/page.tsx', 'r', encoding='utf-8').read()
perfil_content = perfil_content.replace(
    'const API_URL = "http://localhost:8002"',
    'const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8002"'
)
perfil_content = perfil_content.replace(
    'const TOKEN = "user_3I59hLkVRqSndxMj9KVIpYnwhDw"',
    'const TOKEN = process.env.NEXT_PUBLIC_TOKEN || "user_3I59hLkVRqSndxMj9KVIpYnwhDw"'
)
with open('app/perfil/page.tsx', 'w', encoding='utf-8') as f:
    f.write(perfil_content)

print("Variables de entorno configuradas correctamente")