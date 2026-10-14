import json

matches_path = "sports_agents/matches_database.json"
with open(matches_path, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

cl_matches = {
    "Galatasaray vs Barcelona": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "RAMS Park (Estambul, Turquía)",
        "spectators_est": "52,000 en caldera turca (~65M audiencia global)",
        "referee": "Clément Turpin",
        "referee_avg_yellows": 3.9,
        "referee_avg_reds": 0.15,
        "intensity": "Extrema (El infierno de Estambul: Osimhen e Icardi desafiando a Lamine Yamal y Lewandowski)"
    },
    "Arsenal vs Lille": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Emirates Stadium (Londres, Inglaterra)",
        "spectators_est": "60,000 espectadores",
        "referee": "Davide Massa",
        "referee_avg_yellows": 4.1,
        "referee_avg_reds": 0.14,
        "intensity": "Máxima (Arteta y Saka buscando la cima europea frente al bloque de Jonathan David)"
    },
    "Atlético de Madrid vs Manchester United": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Riyadh Air Metropolitano (Madrid, España)",
        "spectators_est": "70,000 espectadores",
        "referee": "István Kovács",
        "referee_avg_yellows": 4.5,
        "referee_avg_reds": 0.20,
        "intensity": "Máxima (Choque de titanes continentales: Julián Álvarez y Griezmann vs Bruno Fernandes)"
    },
    "Inter Milan vs Club Brugge": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "San Siro - Stadio Giuseppe Meazza (Milán, Italia)",
        "spectators_est": "72,000 tifosi",
        "referee": "Slavko Vinčić",
        "referee_avg_yellows": 3.8,
        "referee_avg_reds": 0.12,
        "intensity": "Alta (Lautaro Martínez y Thuram buscando ratificar liderato ante la revelación belga)"
    },
    "Viking FK vs Bayern Munich": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "SR-Bank Arena (Stavanger, Noruega)",
        "spectators_est": "16,000 espectadores",
        "referee": "Artur Soares Dias",
        "referee_avg_yellows": 3.7,
        "referee_avg_reds": 0.10,
        "intensity": "Alta (Harry Kane y Michael Olise comandando el ataque bávaro en territorio escandinavo)"
    },
    "Villarreal vs Napoli": {
        "tournament": "UEFA Champions League - Fase de Liga (Jornada 2)",
        "stadium": "Estadio de la Cerámica (Villarreal, España)",
        "spectators_est": "23,000 espectadores",
        "referee": "Felix Zwayer",
        "referee_avg_yellows": 4.2,
        "referee_avg_reds": 0.16,
        "intensity": "Máxima (Duelo táctico de alto nivel europeo entre el submarino amarillo y los partenopeos)"
    }
}

for k, v in cl_matches.items():
    matches_db[k] = v

with open(matches_path, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)

print(f"Successfully added 6 UEFA Champions League matches to {matches_path}!")
