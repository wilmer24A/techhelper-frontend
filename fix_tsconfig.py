import json

with open('tsconfig.json', 'r') as f:
    config = json.load(f)

config['compilerOptions']['strict'] = False
config['compilerOptions']['noImplicitAny'] = False

with open('tsconfig.json', 'w') as f:
    json.dump(config, f, indent=2)

print("TypeScript strict desactivado")