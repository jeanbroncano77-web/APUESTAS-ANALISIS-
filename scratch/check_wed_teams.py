import json

with open("sports_agents/teams_database.json", encoding="utf-8") as f:
    teams_db = json.load(f)

teams_check = [
    "Manchester City", "Paris Saint-Germain", "PSG",
    "Roma", "AS Roma", "Real Madrid",
    "Liverpool", "LASK",
    "Borussia Dortmund", "Bodø/Glimt", "Bodo/Glimt",
    "Aston Villa", "Fenerbahçe", "Fenerbahce",
    "Feyenoord", "Como"
]

print("Team presence in DB:")
for t in teams_check:
    print(f"  {t}: {'YES' if t in teams_db else 'NO'}")
