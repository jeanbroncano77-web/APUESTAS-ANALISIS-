import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

history = audit.get('history', [])
for i in [198, 199, 200, 201, 209]:
    if i < len(history):
        print(f"Index {i}:", json.dumps(history[i], indent=2))

