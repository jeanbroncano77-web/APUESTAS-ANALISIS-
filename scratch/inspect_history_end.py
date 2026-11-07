import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    audit = json.load(f)

history = audit.get('history', [])
print("Total history items:", len(history))
for h in history[195:]:
    print(f"#{h.get('id')} | {h.get('match')} | Result: {h.get('result')} | Bankroll: {h.get('bankroll_after')}")

