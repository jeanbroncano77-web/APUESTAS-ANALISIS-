import json

matches_path = "sports_agents/matches_database.json"
with open(matches_path, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

wed_cl_matches = {
    "Manchester City vs Paris Saint-Germain": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2 - Choque de Titanes)",
        "stadium": "Etihad Stadium (Mánchester, Inglaterra)",
        "spectators_est": "53,400 en estadio (~80M audiencia global)",
        "referee": "Szymon Marciniak",
        "referee_avg_yellows": 4.0,
        "referee_avg_reds": 0.15,
        "intensity": "Extrema (Erling Haaland y Kevin De Bruyne enfrentando el bloque de Vitinha y Dembélé)"
    },
    "Roma vs Real Madrid": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Stadio Olimpico (Roma, Italia)",
        "spectators_est": "68,000 tifosi",
        "referee": "Anthony Taylor",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.18,
        "intensity": "Máxima (Batalla clásica europea: Paulo Dybala y Dovbyk desafiando a Vinícius Jr., Mbappé y Bellingham)"
    },
    "LASK vs Liverpool": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Raiffeisen Arena (Linz, Austria)",
        "spectators_est": "19,000 espectadores",
        "referee": "François Letexier",
        "referee_avg_yellows": 3.8,
        "referee_avg_reds": 0.12,
        "intensity": "Alta (Mohamed Salah y Luis Díaz comandando el ataque de los Reds en Austria)"
    },
    "Bodø/Glimt vs Borussia Dortmund": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Aspmyra Stadion (Bodø, Noruega)",
        "spectators_est": "8,200 espectadores",
        "referee": "Glenn Nyberg",
        "referee_avg_yellows": 3.9,
        "referee_avg_reds": 0.14,
        "intensity": "Alta (Guirassy y Brandt visitando el círculo polar en un choque de alto ritmo nórdico)"
    },
    "Aston Villa vs Fenerbahçe": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Villa Park (Birmingham, Inglaterra)",
        "spectators_est": "42,000 espectadores",
        "referee": "Jesús Gil Manzano",
        "referee_avg_yellows": 4.4,
        "referee_avg_reds": 0.20,
        "intensity": "Máxima (Unai Emery buscando consolidar la fortaleza de Villa Park ante Mourinho y Džeko)"
    },
    "Feyenoord vs Como": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Stadion Feijenoord - De Kuip (Róterdam, Países Bajos)",
        "spectators_est": "47,500 espectadores",
        "referee": "Espen Eskås",
        "referee_avg_yellows": 3.7,
        "referee_avg_reds": 0.12,
        "intensity": "Alta (La caldera de De Kuip empujando a Santiago Giménez ante la revelación italiana de Fàbregas)"
    }
}

for k, v in wed_cl_matches.items():
    matches_db[k] = v

with open(matches_path, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)

print(f"Added {len(wed_cl_matches)} matches for Wednesday Champions League!")
