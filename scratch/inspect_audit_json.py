import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for k, v in d.items():
    if k != 'history':
        print(f"{k}: {v}")

