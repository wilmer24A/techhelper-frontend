content = open('app/chat/page.tsx', 'r', encoding='utf-8').read()

# Asegura que el contenido se muestra correctamente
old = '''              {m.contenido}
              {m.categoria && <span style={{display:"block",fontSize:"11px",opacity:0.5,marginTop:"4px"}}>{m.categoria}</span>}'''

new = '''              <span style={{display:"block",wordBreak:"break-word"}}>{m.contenido}</span>
              {m.categoria && <span style={{display:"block",fontSize:"11px",opacity:0.5,marginTop:"4px"}}>{m.categoria}</span>}'''

content = content.replace(old, new)

with open('app/chat/page.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("Fix móvil aplicado")