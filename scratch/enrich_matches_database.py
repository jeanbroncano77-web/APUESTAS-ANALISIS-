import json

db_path = "sports_agents/matches_database.json"
try:
    with open(db_path, "r", encoding="utf-8") as f:
        db = json.load(f)
except Exception:
    db = {}

contexts = {
    "Mushuc Runa vs Orense SC": {
        "tournament": "LigaPro Ecuabet • Fase Final (Ecuador)",
        "stadium": "Estadio COAC Mushuc Runa (Echaleche, 3,250 msnm)",
        "spectators_est": "8,500 espectadores (13:30 Hora Ecuador)",
        "referee": "Árbitro Central LigaPro",
        "referee_avg_yellows": 4.8,
        "referee_avg_reds": 0.22,
        "intensity": "Muy Alta (Clima gélido y sol andino a 3,250m; ventaja física para el Poncho frente al calor costero de Orense)"
    },
    "Macará vs Independiente del Valle": {
        "tournament": "LigaPro Ecuabet • Partido Definitorio por el Título",
        "stadium": "Estadio Bellavista de Ambato (2,570 msnm)",
        "spectators_est": "16,000 espectadores (15:30 Hora Ecuador — En vivo por Teleamazonas señal abierta)",
        "referee": "Árbitro FIFA Ecuador",
        "referee_avg_yellows": 4.5,
        "referee_avg_reds": 0.18,
        "intensity": "Máxima (Independiente del Valle se corona campeón con un triunfo ante el aguerrido Macará)"
    },
    "Tottenham Hotspur vs Coventry City": {
        "tournament": "Premier League • Inglaterra",
        "stadium": "Tottenham Hotspur Stadium (Londres)",
        "spectators_est": "62,000 espectadores (14:00 Hora Ecuador)",
        "referee": "Michael Oliver",
        "referee_avg_yellows": 3.8,
        "referee_avg_reds": 0.14,
        "intensity": "Alta (Los Spurs buscan imponer su poderío en casa ante la resistencia del Coventry)"
    },
    "Getafe vs Rayo Vallecano": {
        "tournament": "LaLiga EA Sports • España",
        "stadium": "Estadio Coliseum (Getafe)",
        "spectators_est": "14,500 espectadores (14:00 Hora Ecuador)",
        "referee": "Jesús Gil Manzano",
        "referee_avg_yellows": 5.2,
        "referee_avg_reds": 0.28,
        "intensity": "Extrema (Derbi madrileño de alta tensión táctica, choque físico y pocas concesiones)"
    },
    "Monza vs Cagliari": {
        "tournament": "Serie A • Italia",
        "stadium": "Stadio Brianteo / U-Power Stadium (Monza)",
        "spectators_est": "15,000 espectadores (11:30 Hora Ecuador)",
        "referee": "Daniele Doveri",
        "referee_avg_yellows": 4.4,
        "referee_avg_reds": 0.16,
        "intensity": "Media-Alta (Duelo directo por la permanencia en la máxima categoría del Calcio)"
    },
    "Parma vs Torino": {
        "tournament": "Serie A • Italia",
        "stadium": "Estadio Ennio Tardini (Parma)",
        "spectators_est": "22,000 espectadores (13:45 Hora Ecuador)",
        "referee": "Maurizio Mariani",
        "referee_avg_yellows": 4.6,
        "referee_avg_reds": 0.20,
        "intensity": "Alta (Choque histórico del norte italiano; intensidad en mediocampo y transiciones veloces)"
    }
}

for k, v in contexts.items():
    db[k] = v

with open(db_path, "w", encoding="utf-8") as f_w:
    json.dump(db, f_w, ensure_ascii=False, indent=2)

print("Matches database updated with rich context for the 6 Monday matches.")
