import sys, json
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for r in d['history']:
    if r['status'] == 'loss':
        print(f"Loss: #{r['id']} - {r['match']}: {r['selection']} (tag: {r['category_tag']}, is_fija: {r['is_fija']})")
