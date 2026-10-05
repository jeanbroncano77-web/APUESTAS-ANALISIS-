import json
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

with open('sports_agents/teams_database.json', 'r', encoding='utf-8') as f:
    teams = json.load(f)

for k in sorted(teams.keys()):
    print(f"Team: {k} (Players: {len(teams[k].get('key_players', []))})")
