import json

with open("sports_agents/teams_database.json", encoding="utf-8") as f:
    teams_db = json.load(f)

teams_needed = [
    "Galatasaray", "Barcelona", "FC Barcelona",
    "Arsenal", "Lille", "Lille OSC",
    "Atlético de Madrid", "Atletico Madrid", "Manchester United",
    "Inter Milan", "Inter de Milán", "Club Brugge",
    "Viking FK", "Bayern Munich",
    "Villarreal", "Napoli", "SSC Napoli",
    "RB Leipzig", "PSV Eindhoven"
]

print("Teams found in DB:")
for t in teams_needed:
    if t in teams_db:
        print(f"  [YES] {t}")
    else:
        print(f"  [NO ] {t}")
