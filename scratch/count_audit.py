import json

with open('sports_agents/audit_history.json', 'r', encoding='utf-8') as f:
    audit_data = json.load(f)

history = audit_data.get('history', [])
print("Total history rows:", len(history))

wins = sum(1 for r in history if r.get('status') == 'win')
losses = sum(1 for r in history if r.get('status') == 'loss')
print(f"Wins: {wins}, Losses: {losses}")

fijas = sum(1 for r in history if r.get('is_fija'))
fija_losses = sum(1 for r in history if r.get('is_fija') and r.get('status') == 'loss')
print(f"Fijas total: {fijas}, Fijas losses: {fija_losses}")

cat_counts = {}
for r in history:
    cat = r.get('category_tag', '')
    cat_counts[cat] = cat_counts.get(cat, 0) + 1

print("\nCategories:")
for k, v in cat_counts.items():
    print(f"  {k}: {v}")
