import json

with open("sports_agents/simulations_tomorrow_results.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Target: {data.get('TargetDay')} {data.get('TargetDate')}")
for m in data["Matches"]:
    print(f"\n==========================================")
    print(f"MATCH: {m['match']}")
    h_veto = [f"{v['name']} [{v['injury']}]" for v in m['squad_health']['home_vetoed']]
    a_veto = [f"{v['name']} [{v['injury']}]" for v in m['squad_health']['away_vetoed']]
    if h_veto:
        print(f"  [BAJAS LOCAL]: {', '.join(h_veto)}")
    else:
        print(f"  [LOCAL]: 100% Plantel Sano")
    if a_veto:
        print(f"  [BAJAS VISITA]: {', '.join(a_veto)}")
    else:
        print(f"  [VISITA]: 100% Plantel Sano")
    
    h_props = [f"{p['name']} ({p['expected_shots']} tiros, {p['expected_sot']} a puerta)" for p in m['player_props']['home_key_players']]
    a_props = [f"{p['name']} ({p['expected_shots']} tiros, {p['expected_sot']} a puerta)" for p in m['player_props']['away_key_players']]
    print(f"  PROPS LOCAL: {', '.join(h_props)}")
    print(f"  PROPS VISITA: {', '.join(a_props)}")
