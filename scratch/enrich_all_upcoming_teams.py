# -*- coding: utf-8 -*-
"""
enrich_all_upcoming_teams.py
Inyecta todos los perfiles de equipos de la Liga Argentina y Sudamérica en teams_database.json,
metadatos de partidos en matches_database.json y un calendario robusto de 3 semanas en official_calendar.json.
"""
import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
teams_file = os.path.join(base_dir, "sports_agents", "teams_database.json")
matches_file = os.path.join(base_dir, "sports_agents", "matches_database.json")
cal_file = os.path.join(base_dir, "sports_agents", "official_calendar.json")

new_teams = {
    "Lanús": {
        "fifa_rank": 22,
        "recent_form": ["W", "W", "D", "L", "W", "D", "W", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.75, "xg_against": 1.10, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.40, "xg_against": 0.85, "corners_for": 5, "corners_against": 3, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 52},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.30, "xg_against": 1.20, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.85, "xg_against": 0.75, "corners_for": 7, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 56}
        ],
        "key_players": [
            {"name": "Walter Bou", "position": "Delantero Centro Goleador", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 3.1, "goal_prob": 0.38},
            {"name": "Marcelino Moreno", "position": "Mediapunta Talentoso", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.8, "goal_prob": 0.28},
            {"name": "Carlos Izquierdoz", "position": "Defensa Central Líder", "avg_shots_p90": 0.8, "avg_sot_p90": 0.3, "shot_creation_actions": 1.2, "goal_prob": 0.08}
        ]
    },
    "Godoy Cruz": {
        "fifa_rank": 28,
        "recent_form": ["D", "W", "L", "W", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.25, "xg_against": 1.20, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 49},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.60, "xg_against": 0.90, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 52},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.85, "xg_against": 1.35, "corners_for": 3, "corners_against": 6, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 46}
        ],
        "key_players": [
            {"name": "Salomón Rodríguez", "position": "Delantero Tanque", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 2.2, "goal_prob": 0.32},
            {"name": "Daniel Barrea", "position": "Extremo Ofensivo", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.4, "goal_prob": 0.22},
            {"name": "Nicolás Fernández", "position": "Volante Mixto", "avg_shots_p90": 1.2, "avg_sot_p90": 0.5, "shot_creation_actions": 3.6, "goal_prob": 0.14}
        ]
    },
    "Central Córdoba": {
        "fifa_rank": 42,
        "recent_form": ["W", "D", "W", "L", "D", "W", "D", "L"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.20, "xg_against": 0.95, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.10, "xg_against": 1.15, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 48},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.45, "xg_against": 1.05, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50}
        ],
        "key_players": [
            {"name": "Matías Godoy", "position": "Extremo Habilidoso", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 3.8, "goal_prob": 0.28},
            {"name": "Lucas Varaldo", "position": "Punta Definidor", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.4, "goal_prob": 0.30},
            {"name": "Rodrigo Atencio", "position": "Volante Ofensivo", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.9, "goal_prob": 0.20}
        ]
    },
    "Belgrano": {
        "fifa_rank": 35,
        "recent_form": ["D", "W", "L", "D", "W", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.30, "xg_against": 1.25, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 50},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.65, "xg_against": 0.85, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.90, "xg_against": 1.30, "corners_for": 4, "corners_against": 5, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 47}
        ],
        "key_players": [
            {"name": "Franco Jara", "position": "Goleador Pirata", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 2.7, "goal_prob": 0.36},
            {"name": "Nicolás Fernández", "position": "Uvita / Delantero Rápido", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.2, "goal_prob": 0.30},
            {"name": "Francisco González Metilli", "position": "Volante Creativo", "avg_shots_p90": 1.7, "avg_sot_p90": 0.6, "shot_creation_actions": 4.0, "goal_prob": 0.18}
        ]
    },
    "Independiente": {
        "fifa_rank": 20,
        "recent_form": ["W", "D", "W", "W", "D", "D", "W", "L"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.80, "xg_against": 0.70, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.45, "xg_against": 1.10, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 54},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.50, "xg_against": 0.80, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 55}
        ],
        "key_players": [
            {"name": "Gabriel Ávalos", "position": "Delantero de Área", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.5, "goal_prob": 0.38},
            {"name": "Santiago Montiel", "position": "Extremo Punzante", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.1, "goal_prob": 0.25},
            {"name": "Felipe Loyola", "position": "Volante Dinámico", "avg_shots_p90": 1.5, "avg_sot_p90": 0.6, "shot_creation_actions": 3.6, "goal_prob": 0.16}
        ]
    },
    "Newell's Old Boys": {
        "fifa_rank": 33,
        "recent_form": ["L", "D", "W", "L", "D", "W", "L", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.20, "xg_against": 1.20, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 48},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.90, "xg_against": 1.30, "corners_for": 4, "corners_against": 5, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 47},
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.50, "xg_against": 1.10, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51}
        ],
        "key_players": [
            {"name": "Juan Manuel García", "position": "Delantero de Choque", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 2.2, "goal_prob": 0.30},
            {"name": "Éver Banega", "position": "Cerebro y Capitán", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 5.2, "goal_prob": 0.18},
            {"name": "Francisco González", "position": "Extremo Eléctrico", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.4, "goal_prob": 0.22}
        ]
    },
    "Argentinos Juniors": {
        "fifa_rank": 24,
        "recent_form": ["W", "D", "L", "W", "D", "W", "W", "L"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.75, "xg_against": 0.80, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 57},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.35, "xg_against": 1.15, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 55},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.50, "xg_against": 0.75, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 56}
        ],
        "key_players": [
            {"name": "Maximiliano Romero", "position": "Delantero Oportunista", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 2.6, "goal_prob": 0.35},
            {"name": "Alan Lescano", "position": "Mediapunta Goleador", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 4.0, "goal_prob": 0.30},
            {"name": "Nicolás Oroz", "position": "Organizador Zurdo", "avg_shots_p90": 1.5, "avg_sot_p90": 0.5, "shot_creation_actions": 4.4, "goal_prob": 0.16}
        ]
    },
    "Talleres": {
        "fifa_rank": 19,
        "recent_form": ["W", "W", "D", "W", "D", "L", "W", "W"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.80, "xg_against": 1.05, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 55},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.55, "xg_against": 0.80, "corners_for": 5, "corners_against": 3, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53},
            {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.90, "xg_against": 0.70, "corners_for": 7, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 58}
        ],
        "key_players": [
            {"name": "Federico Girotti", "position": "Centrodelantero de Poder", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.4, "goal_prob": 0.38},
            {"name": "Rubén Botta", "position": "10 Clásico de Gran Visión", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 5.1, "goal_prob": 0.25},
            {"name": "Gastón Benavídez", "position": "Lateral Ofensivo", "avg_shots_p90": 1.2, "avg_sot_p90": 0.4, "shot_creation_actions": 3.3, "goal_prob": 0.12}
        ]
    },
    "Platense": {
        "fifa_rank": 38,
        "recent_form": ["D", "W", "L", "D", "W", "D", "L", "D"],
        "sequence": [
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.15, "xg_against": 0.90, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 46},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.10, "xg_against": 1.15, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 47},
            {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.80, "xg_against": 1.25, "corners_for": 3, "corners_against": 5, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 45}
        ],
        "key_players": [
            {"name": "Mateo Pellegrino", "position": "Delantero Referente", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 2.3, "goal_prob": 0.32},
            {"name": "Guido Mainero", "position": "Volante con Llegada", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.5, "goal_prob": 0.22},
            {"name": "Ignacio Vázquez", "position": "Líder de la Zaga", "avg_shots_p90": 0.7, "avg_sot_p90": 0.3, "shot_creation_actions": 1.0, "goal_prob": 0.08}
        ]
    },
    "Rosario Central": {
        "fifa_rank": 29,
        "recent_form": ["W", "L", "D", "W", "D", "L", "W", "D"],
        "sequence": [
            {"goals_scored": 2, "goals_conceded": 1, "xg_for": 1.60, "xg_against": 1.10, "corners_for": 5, "corners_against": 4, "shots_total": 12, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 52},
            {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.40, "xg_against": 0.85, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 51},
            {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.25, "xg_against": 1.20, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 49}
        ],
        "key_players": [
            {"name": "Ignacio Malcorra", "position": "Generador de Juego", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 4.9, "goal_prob": 0.26},
            {"name": "Jaminton Campaz", "position": "Extremo Colombiano Desequilibrante", "avg_shots_p90": 2.6, "avg_sot_p90": 1.1, "shot_creation_actions": 4.2, "goal_prob": 0.30},
            {"name": "Marco Ruben", "position": "Ídolo y Definidor de Área", "avg_shots_p90": 2.2, "avg_sot_p90": 1.0, "shot_creation_actions": 2.1, "goal_prob": 0.34}
        ]
    }
}

with open(teams_file, "r", encoding="utf-8") as f:
    teams_db = json.load(f)

for t_k, t_v in new_teams.items():
    teams_db[t_k] = t_v

with open(teams_file, "w", encoding="utf-8") as f:
    json.dump(teams_db, f, ensure_ascii=False, indent=2)
print(f"-> {len(new_teams)} perfiles de equipos inyectados en teams_database.json (Total ahora: {len(teams_db)}).")

# Actualizar partidos en matches_database.json
new_matches_info = {
    "River Plate vs Vélez Sarsfield": {
        "tournament": "Liga Profesional Argentina - Fecha 12",
        "stadium": "Estadio Monumental (Buenos Aires)",
        "spectators_est": "84,500 en estadio (~25M audiencia)",
        "referee": "Facundo Tello",
        "referee_avg_yellows": 4.3,
        "referee_avg_reds": 0.15,
        "intensity": "Máxima (Choque en la cima; River busca hacer valer el Monumental ante el líder Vélez)"
    },
    "Racing Club vs San Lorenzo": {
        "tournament": "Liga Profesional Argentina - Fecha 12",
        "stadium": "Estadio Presidente Perón (El Cilindro, Avellaneda)",
        "spectators_est": "50,000 en estadio (~18M audiencia)",
        "referee": "Yael Falcón Pérez",
        "referee_avg_yellows": 4.7,
        "referee_avg_reds": 0.20,
        "intensity": "Clásico de Alta Tensión (La Academia de Costas ante el Ciclón de Romagnoli)"
    },
    "Lanús vs Godoy Cruz": {
        "tournament": "Liga Profesional Argentina - Fecha 12",
        "stadium": "Estadio Ciudad de Lanús (La Fortaleza)",
        "spectators_est": "25,000 en estadio (~10M audiencia)",
        "referee": "Fernando Rapallini",
        "referee_avg_yellows": 4.1,
        "referee_avg_reds": 0.14,
        "intensity": "Alta (La Fortaleza de Lanús ante el Tomba mendocino en lucha por copas)"
    },
    "Central Córdoba vs Belgrano": {
        "tournament": "Liga Profesional Argentina - Fecha 12",
        "stadium": "Estadio Madre de Ciudades (Santiago del Estero)",
        "spectators_est": "28,000 en estadio (~9M audiencia)",
        "referee": "Andrés Merlos",
        "referee_avg_yellows": 4.5,
        "referee_avg_reds": 0.18,
        "intensity": "Alta (Duelo de estilos; bloque cerrado de Santiago ante la pegada de Franco Jara)"
    },
    "Independiente vs Newell's Old Boys": {
        "tournament": "Liga Profesional Argentina - Fecha 12",
        "stadium": "Estadio Libertadores de América (Avellaneda)",
        "spectators_est": "42,000 en estadio (~16M audiencia)",
        "referee": "Leandro Rey Hilfer",
        "referee_avg_yellows": 4.6,
        "referee_avg_reds": 0.16,
        "intensity": "Muy Alta (El Rojo de Vaccari busca ratificar su gran racha de local ante la Lepra de Banega)"
    },
    "Argentinos Juniors vs Talleres": {
        "tournament": "Liga Profesional Argentina - Fecha 12",
        "stadium": "Estadio Diego Armando Maradona (La Paternal)",
        "spectators_est": "15,000 en estadio (~12M audiencia)",
        "referee": "Silvio Trucco",
        "referee_avg_yellows": 4.4,
        "referee_avg_reds": 0.15,
        "intensity": "Muy Alta (Duelo técnico en La Paternal; posesión del Bicho ante la velocidad de Girotti y Botta)"
    }
}

with open(matches_file, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

for mk, mv in new_matches_info.items():
    matches_db[mk] = mv

with open(matches_file, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)
print("-> Metadatos de partidos de Sábado guardados en matches_database.json.")
