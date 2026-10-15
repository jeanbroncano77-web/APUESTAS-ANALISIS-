import json
import os

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
teams_file = os.path.join(base_dir, "sports_agents", "teams_database.json")

with open(teams_file, "r", encoding="utf-8") as f:
    teams = json.load(f)

new_teams = {
    "AC Milan": {
        "league": "Serie A (Italia)",
        "elo": 1845,
        "attack_rating": 86,
        "defense_rating": 84,
        "form_last_5": ["W", "W", "D", "W", "L"],
        "xg_for_avg": 1.95,
        "xg_against_avg": 1.10,
        "key_players": ["Rafael Leão", "Christian Pulisic", "Theo Hernández", "Mike Maignan"],
        "home_advantage": 1.14
    },
    "Red Bull Salzburg": {
        "league": "Austrian Bundesliga",
        "elo": 1690,
        "attack_rating": 78,
        "defense_rating": 75,
        "form_last_5": ["W", "L", "D", "W", "W"],
        "xg_for_avg": 1.60,
        "xg_against_avg": 1.35,
        "key_players": ["Oscar Gloukh", "Karim Konaté", "Lucas Gourna-Douath"],
        "home_advantage": 1.10
    },
    "Juventus": {
        "league": "Serie A (Italia)",
        "elo": 1830,
        "attack_rating": 84,
        "defense_rating": 88,
        "form_last_5": ["W", "D", "W", "W", "D"],
        "xg_for_avg": 1.75,
        "xg_against_avg": 0.85,
        "key_players": ["Dušan Vlahović", "Kenan Yıldız", "Bremer", "Teun Koopmeiners"],
        "home_advantage": 1.15
    },
    "Celta Vigo": teams.get("Celta de Vigo", {
        "league": "LaLiga (España)",
        "elo": 1680,
        "attack_rating": 77,
        "defense_rating": 76,
        "form_last_5": ["D", "L", "W", "D", "L"],
        "xg_for_avg": 1.40,
        "xg_against_avg": 1.45,
        "key_players": ["Iago Aspas", "Tasos Douvikas", "Óscar Mingueza"],
        "home_advantage": 1.12
    }),
    "Benfica": {
        "league": "Liga Portugal",
        "elo": 1820,
        "attack_rating": 86,
        "defense_rating": 83,
        "form_last_5": ["W", "W", "W", "D", "W"],
        "xg_for_avg": 2.15,
        "xg_against_avg": 0.95,
        "key_players": ["Ángel Di María", "Vangelis Pavlidis", "Orkun Kökçü", "Florentino"],
        "home_advantage": 1.20
    },
    "Celtic": {
        "league": "Scottish Premiership",
        "elo": 1710,
        "attack_rating": 80,
        "defense_rating": 76,
        "form_last_5": ["W", "W", "W", "L", "W"],
        "xg_for_avg": 2.20,
        "xg_against_avg": 1.25,
        "key_players": ["Kyogo Furuhashi", "Daizen Maeda", "Reo Hatate", "Callum McGregor"],
        "home_advantage": 1.18
    },
    "Bayer Leverkusen": {
        "league": "Bundesliga (Alemania)",
        "elo": 1865,
        "attack_rating": 88,
        "defense_rating": 83,
        "form_last_5": ["W", "D", "W", "W", "W"],
        "xg_for_avg": 2.30,
        "xg_against_avg": 1.15,
        "key_players": ["Florian Wirtz", "Victor Boniface", "Jeremie Frimpong", "Granit Xhaka"],
        "home_advantage": 1.16
    },
    "Lech Poznań": {
        "league": "Ekstraklasa (Polonia)",
        "elo": 1630,
        "attack_rating": 74,
        "defense_rating": 73,
        "form_last_5": ["W", "W", "D", "L", "W"],
        "xg_for_avg": 1.55,
        "xg_against_avg": 1.20,
        "key_players": ["Mikael Ishak", "Afonso Sousa", "Dino Hotić"],
        "home_advantage": 1.14
    },
    "Olympique Lyon": {
        "league": "Ligue 1 (Francia)",
        "elo": 1765,
        "attack_rating": 82,
        "defense_rating": 79,
        "form_last_5": ["W", "W", "L", "W", "D"],
        "xg_for_avg": 1.85,
        "xg_against_avg": 1.30,
        "key_players": ["Alexandre Lacazette", "Rayan Cherki", "Georges Mikautadze", "Corentin Tolisso"],
        "home_advantage": 1.16
    },
    "AFC Ajax": {
        "league": "Eredivisie (Países Bajos)",
        "elo": 1770,
        "attack_rating": 83,
        "defense_rating": 78,
        "form_last_5": ["W", "W", "D", "W", "W"],
        "xg_for_avg": 2.05,
        "xg_against_avg": 1.15,
        "key_players": ["Brian Brobbey", "Kenneth Taylor", "Jordan Henderson", "Bertrand Traoré"],
        "home_advantage": 1.15
    },
    "Hajduk Split": {
        "league": "HNL (Croacia)",
        "elo": 1640,
        "attack_rating": 75,
        "defense_rating": 74,
        "form_last_5": ["W", "D", "W", "W", "D"],
        "xg_for_avg": 1.50,
        "xg_against_avg": 1.05,
        "key_players": ["Marko Livaja", "Ivan Rakitić", "Filip Krovinović"],
        "home_advantage": 1.18
    }
}

teams.update(new_teams)

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams, f, indent=2, ensure_ascii=False)

print(f"teams_database.json actualizado con {len(new_teams)} equipos de Europa League y Conference League. Total: {len(teams)}")
