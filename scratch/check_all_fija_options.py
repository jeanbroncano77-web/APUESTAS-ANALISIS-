import json

with open('sports_agents/simulations_tomorrow_results.json', encoding='utf-8') as f:
    data = json.load(f)

for m in data['Matches']:
    print(f"\n=== {m['match']} ===")
    opts = m.get('all_fija_options', [])
    for opt in opts:
        print(f"  * {opt.get('category_code')}: {opt.get('selection')} | Prob: {opt.get('probability')}% | Cuota: @{opt.get('odds')} | Score: {opt.get('_rank_score')}")
