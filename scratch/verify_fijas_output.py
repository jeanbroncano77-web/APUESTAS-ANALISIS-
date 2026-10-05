import json

with open('sports_agents/simulations_tomorrow_results.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"Generated at: {data.get('GeneratedAt')}")
print(f"Target: {data.get('TargetDay')} {data.get('TargetDate')}")
print("=" * 65)
for i, m in enumerate(data['Matches'], 1):
    fija = m['la_fija_real']
    prob = fija['probability']
    status = "OK [95.0% - 98.2%]" if 95.0 <= prob <= 98.2 else "ALERTA FUERA DE RANGO"
    print(f"[{i}] {m['match']}")
    print(f"    Selección: {fija['selection']}")
    print(f"    Mercado:   {fija['market']}")
    print(f"    Prob:      {prob}%  |  Cuota: @{fija['odds']}")
    print(f"    Estado:    {status}")
    print(f"    Rationale: {fija.get('rationale')}")
    print("-" * 65)
