import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

h = data.get('history', [])
print(f"Total rows: {len(h)}")
wins = [x for x in h if x.get('status') == 'win']
losses = [x for x in h if x.get('status') == 'loss']
print(f"Wins: {len(wins)}, Losses: {len(losses)}")

fijas = [x for x in h if x.get('is_fija')]
fijas_wins = [x for x in fijas if x.get('status') == 'win']
fijas_losses = [x for x in fijas if x.get('status') == 'loss']
print(f"Fijas Total: {len(fijas)}, Fijas Wins: {len(fijas_wins)}, Fijas Losses: {len(fijas_losses)}")
print("Fija losses:")
for l in fijas_losses:
    print(f"  #{l.get('id')}: {l.get('match')} -> {l.get('selection')}")

print("\nAll losses:")
for l in losses:
    print(f"  #{l.get('id')}: {l.get('match')} -> {l.get('selection')} (is_fija={l.get('is_fija')})")

# Check all categories
categories = {}
for r in h:
    tag = r.get('category_tag', 'Otro')
    categories[tag] = categories.get(tag, 0) + 1
print("\nCategories counts:")
for cat, count in categories.items():
    print(f"  {cat}: {count}")
