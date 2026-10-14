import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

print("Total history:", len(d.get("history", [])))
for r in d.get("history", [])[-10:]:
    print(f"#{r['id']}: {r['match']} | {r['selection']} | {r['status']}")
