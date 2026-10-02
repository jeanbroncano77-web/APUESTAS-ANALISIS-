# -*- coding: utf-8 -*-
import os
import re

agent_file = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo\sports_agents\data_scout_agent.py"

with open(agent_file, "r", encoding="utf-8") as f:
    code = f.read()

# Equipos de Viernes a insertar antes de "        return histories.get(team_name, {})"
friday_teams_code = """
            # --- VIERNES ESTELAR: DORTMUND VS ST. PAULI ---
            "St. Pauli": {
                "fifa_rank": 82,
                "recent_form": ["L", "L", "W", "D", "L"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.6, "xg_against": 2.4, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 41},
                    {"goals_scored": 3, "goals_conceded": 0, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 1, "red_cards": 0, "fouls": 12, "possession": 52},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 1.1, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44},
                ],
                "key_players": [
                    {"name": "Johannes Eggestein", "position": "Delantero Móvil", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.8, "goal_prob": 0.28},
                    {"name": "Morgan Guilavogui", "position": "Extremo Potente", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.4, "goal_prob": 0.30},
                    {"name": "Jackson Irvine", "position": "Capitán / Box-to-Box", "avg_shots_p90": 1.6, "avg_sot_p90": 0.6, "shot_creation_actions": 3.8, "goal_prob": 0.20}
                ]
            },

            # --- VIERNES ESTELAR: NAPOLI VS COMO ---
            "Napoli": {
                "fifa_rank": 14,
                "recent_form": ["W", "W", "D", "W", "W", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 2.5, "xg_against": 0.5, "corners_for": 7, "corners_against": 3, "shots_total": 17, "shots_on_target": 7, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 63},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.4, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 13, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 56},
                    {"goals_scored": 4, "goals_conceded": 0, "xg_for": 3.1, "xg_against": 0.4, "corners_for": 8, "corners_against": 2, "shots_total": 19, "shots_on_target": 9, "yellow_cards": 1, "red_cards": 0, "fouls": 9, "possession": 65},
                    {"goals_scored": 2, "goals_conceded": 1, "xg_for": 2.2, "xg_against": 0.8, "corners_for": 6, "corners_against": 3, "shots_total": 15, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 60}
                ],
                "key_players": [
                    {"name": "Khvicha Kvaratskhelia", "position": "Extremo Gambeteador", "avg_shots_p90": 3.6, "avg_sot_p90": 1.7, "shot_creation_actions": 6.5, "goal_prob": 0.55},
                    {"name": "Romelu Lukaku", "position": "Boya / Ariete Físico", "avg_shots_p90": 3.2, "avg_sot_p90": 1.8, "shot_creation_actions": 3.4, "goal_prob": 0.62},
                    {"name": "Matteo Politano", "position": "Extremo Diestro Incisivo", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 4.8, "goal_prob": 0.28},
                    {"name": "Scott McTominay", "position": "Volante Llegador", "avg_shots_p90": 2.3, "avg_sot_p90": 1.1, "shot_creation_actions": 3.1, "goal_prob": 0.34}
                ]
            },
            "Como": {
                "fifa_rank": 88,
                "recent_form": ["W", "W", "D", "L", "D"],
                "sequence": [
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 1.9, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 53},
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.1, "xg_against": 1.6, "corners_for": 5, "corners_against": 6, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 52},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.5, "xg_against": 1.8, "corners_for": 4, "corners_against": 6, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 48}
                ],
                "key_players": [
                    {"name": "Patrick Cutrone", "position": "Delantero Rematador", "avg_shots_p90": 2.8, "avg_sot_p90": 1.3, "shot_creation_actions": 2.7, "goal_prob": 0.40},
                    {"name": "Gabriel Strefezza", "position": "Extremo / Creador", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 4.6, "goal_prob": 0.26},
                    {"name": "Nico Paz", "position": "Joya Mediapunta", "avg_shots_p90": 2.6, "avg_sot_p90": 1.2, "shot_creation_actions": 5.2, "goal_prob": 0.32}
                ]
            },

            # --- VIERNES ESTELAR: MARSEILLE VS ANGERS ---
            "Marseille": {
                "fifa_rank": 26,
                "recent_form": ["L", "W", "W", "W", "D", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 1.2, "xg_against": 1.3, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 65},
                    {"goals_scored": 3, "goals_conceded": 2, "xg_for": 2.4, "xg_against": 1.5, "corners_for": 5, "corners_against": 6, "shots_total": 15, "shots_on_target": 7, "yellow_cards": 3, "red_cards": 1, "fouls": 14, "possession": 58},
                    {"goals_scored": 3, "goals_conceded": 1, "xg_for": 2.7, "xg_against": 0.9, "corners_for": 7, "corners_against": 3, "shots_total": 18, "shots_on_target": 8, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 62}
                ],
                "key_players": [
                    {"name": "Mason Greenwood", "position": "Extremo Goleador", "avg_shots_p90": 3.8, "avg_sot_p90": 1.9, "shot_creation_actions": 4.9, "goal_prob": 0.60},
                    {"name": "Elye Wahi", "position": "Delantero Centro Rápido", "avg_shots_p90": 2.7, "avg_sot_p90": 1.3, "shot_creation_actions": 2.6, "goal_prob": 0.42},
                    {"name": "Amine Harit", "position": "Organizador Creativo", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 5.8, "goal_prob": 0.24},
                    {"name": "Luis Henrique", "position": "Extremo Desborde", "avg_shots_p90": 2.2, "avg_sot_p90": 1.1, "shot_creation_actions": 4.4, "goal_prob": 0.32}
                ]
            },
            "Angers": {
                "fifa_rank": 95,
                "recent_form": ["L", "D", "D", "D", "L"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 3, "xg_for": 0.9, "xg_against": 2.5, "corners_for": 4, "corners_against": 7, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 42},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.1, "xg_against": 1.3, "corners_for": 4, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 46},
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 1.0, "xg_against": 1.4, "corners_for": 3, "corners_against": 6, "shots_total": 8, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 44}
                ],
                "key_players": [
                    {"name": "Himad Abdelli", "position": "Enganche / Creativo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 4.2, "goal_prob": 0.25},
                    {"name": "Farid El Melali", "position": "Extremo Rápido", "avg_shots_p90": 2.0, "avg_sot_p90": 0.7, "shot_creation_actions": 3.1, "goal_prob": 0.22},
                    {"name": "Lois Diony", "position": "Delantero Centro", "avg_shots_p90": 1.9, "avg_sot_p90": 0.8, "shot_creation_actions": 2.0, "goal_prob": 0.24}
                ]
            },

            # --- VIERNES ESTELAR: LEGANÉS VS VALENCIA ---
            "Leganés": {
                "fifa_rank": 78,
                "recent_form": ["D", "L", "L", "L", "D"],
                "sequence": [
                    {"goals_scored": 1, "goals_conceded": 1, "xg_for": 0.8, "xg_against": 1.2, "corners_for": 4, "corners_against": 5, "shots_total": 9, "shots_on_target": 3, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 44},
                    {"goals_scored": 0, "goals_conceded": 2, "xg_for": 0.6, "xg_against": 1.8, "corners_for": 3, "corners_against": 6, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 2, "red_cards": 0, "fouls": 13, "possession": 41},
                    {"goals_scored": 0, "goals_conceded": 1, "xg_for": 0.7, "xg_against": 1.4, "corners_for": 4, "corners_against": 5, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 4, "red_cards": 0, "fouls": 16, "possession": 43}
                ],
                "key_players": [
                    {"name": "Juan Cruz", "position": "Extremo Desequilibrante", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.8, "goal_prob": 0.30},
                    {"name": "Dani Raba", "position": "Mediapunta Zurdo", "avg_shots_p90": 2.1, "avg_sot_p90": 0.8, "shot_creation_actions": 3.5, "goal_prob": 0.24},
                    {"name": "Miguel de la Fuente", "position": "Delantero de Choque", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 2.2, "goal_prob": 0.28}
                ]
            },
            "Valencia": {
                "fifa_rank": 38,
                "recent_form": ["L", "D", "W", "L", "D"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 3, "xg_for": 0.7, "xg_against": 2.2, "corners_for": 3, "corners_against": 7, "shots_total": 8, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 14, "possession": 42},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.1, "xg_against": 1.0, "corners_for": 5, "corners_against": 4, "shots_total": 11, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 50},
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.8, "xg_against": 0.7, "corners_for": 6, "corners_against": 3, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 53}
                ],
                "key_players": [
                    {"name": "Hugo Duro", "position": "Ariete Luchador", "avg_shots_p90": 2.5, "avg_sot_p90": 1.2, "shot_creation_actions": 2.4, "goal_prob": 0.38},
                    {"name": "Diego López", "position": "Extremo / Segundo Punta", "avg_shots_p90": 2.2, "avg_sot_p90": 0.9, "shot_creation_actions": 3.9, "goal_prob": 0.28},
                    {"name": "Pepelu", "position": "Metrónomo & Balón Parado", "avg_shots_p90": 1.4, "avg_sot_p90": 0.5, "shot_creation_actions": 4.5, "goal_prob": 0.18},
                    {"name": "Javi Guerra", "position": "Interior Box-to-Box", "avg_shots_p90": 1.8, "avg_sot_p90": 0.7, "shot_creation_actions": 3.4, "goal_prob": 0.22}
                ]
            },

            # --- VIERNES ESTELAR: SUNDERLAND VS LEEDS UNITED ---
            "Sunderland": {
                "fifa_rank": 65,
                "recent_form": ["W", "W", "L", "W", "W"],
                "sequence": [
                    {"goals_scored": 2, "goals_conceded": 0, "xg_for": 1.9, "xg_against": 0.8, "corners_for": 6, "corners_against": 4, "shots_total": 14, "shots_on_target": 6, "yellow_cards": 2, "red_cards": 0, "fouls": 11, "possession": 54},
                    {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.3, "xg_against": 1.7, "corners_for": 5, "corners_against": 5, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 3, "red_cards": 0, "fouls": 13, "possession": 49},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.5, "xg_against": 0.6, "corners_for": 7, "corners_against": 3, "shots_total": 13, "shots_on_target": 5, "yellow_cards": 1, "red_cards": 0, "fouls": 10, "possession": 56}
                ],
                "key_players": [
                    {"name": "Jobe Bellingham", "position": "Volante Llegador", "avg_shots_p90": 2.4, "avg_sot_p90": 1.0, "shot_creation_actions": 3.8, "goal_prob": 0.32},
                    {"name": "Wilson Isidor", "position": "Delantero Rápido", "avg_shots_p90": 2.6, "avg_sot_p90": 1.3, "shot_creation_actions": 2.5, "goal_prob": 0.40},
                    {"name": "Romaine Mundle", "position": "Extremo Eléctrico", "avg_shots_p90": 2.7, "avg_sot_p90": 1.2, "shot_creation_actions": 4.6, "goal_prob": 0.36},
                    {"name": "Chris Rigg", "position": "Talento Creativo", "avg_shots_p90": 1.7, "avg_sot_p90": 0.7, "shot_creation_actions": 4.1, "goal_prob": 0.22}
                ]
            },

            # --- VIERNES ESTELAR: RIO AVE VS FAMALICÃO ---
            "Rio Ave": {
                "fifa_rank": 79,
                "recent_form": ["L", "D", "W", "L", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 4, "xg_for": 0.5, "xg_against": 2.8, "corners_for": 3, "corners_against": 7, "shots_total": 7, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 16, "possession": 38},
                    {"goals_scored": 2, "goals_conceded": 2, "xg_for": 1.6, "xg_against": 1.5, "corners_for": 5, "corners_against": 5, "shots_total": 12, "shots_on_target": 5, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 51},
                    {"goals_scored": 1, "goals_conceded": 0, "xg_for": 1.4, "xg_against": 0.9, "corners_for": 6, "corners_against": 4, "shots_total": 11, "shots_on_target": 4, "yellow_cards": 2, "red_cards": 0, "fouls": 12, "possession": 53}
                ],
                "key_players": [
                    {"name": "Clayton", "position": "Delantero Centro", "avg_shots_p90": 2.5, "avg_sot_p90": 1.1, "shot_creation_actions": 2.6, "goal_prob": 0.36},
                    {"name": "Kiko Bondoso", "position": "Extremo Rápido", "avg_shots_p90": 2.1, "avg_sot_p90": 0.9, "shot_creation_actions": 3.7, "goal_prob": 0.26},
                    {"name": "Tiago Morais", "position": "Extremo Incisivo", "avg_shots_p90": 2.3, "avg_sot_p90": 1.0, "shot_creation_actions": 3.4, "goal_prob": 0.28}
                ]
            },
            "Famalicão": {
                "fifa_rank": 74,
                "recent_form": ["D", "D", "L", "W", "W"],
                "sequence": [
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 0.9, "xg_against": 0.8, "corners_for": 4, "corners_against": 4, "shots_total": 9, "shots_on_target": 2, "yellow_cards": 3, "red_cards": 0, "fouls": 15, "possession": 49},
                    {"goals_scored": 0, "goals_conceded": 0, "xg_for": 1.0, "xg_against": 1.1, "corners_for": 5, "corners_against": 5, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 4, "red_cards": 0, "fouls": 17, "possession": 48},
                    {"goals_scored": 1, "goals_conceded": 2, "xg_for": 1.2, "xg_against": 1.6, "corners_for": 4, "corners_against": 6, "shots_total": 10, "shots_on_target": 3, "yellow_cards": 2, "red_cards": 0, "fouls": 14, "possession": 47}
                ],
                "key_players": [
                    {"name": "Mario González", "position": "Ariete Español", "avg_shots_p90": 2.4, "avg_sot_p90": 1.1, "shot_creation_actions": 2.2, "goal_prob": 0.35},
                    {"name": "Zaydou Youssouf", "position": "Pivote Físico", "avg_shots_p90": 1.5, "avg_sot_p90": 0.5, "shot_creation_actions": 3.2, "goal_prob": 0.16},
                    {"name": "Gil Dias", "position": "Extremo Zurdo", "avg_shots_p90": 2.0, "avg_sot_p90": 0.8, "shot_creation_actions": 3.6, "goal_prob": 0.24}
                ]
            }
"""

# Insertar antes de "        return histories.get(team_name, {})"
marker_hist = "        return histories.get(team_name, {})"
if "St. Pauli" not in code:
    code = code.replace(marker_hist, friday_teams_code + "\n" + marker_hist)

# Contextos de partido de Viernes
friday_contexts = """
            ("Borussia Dortmund", "St. Pauli"): {
                "tournament": "Bundesliga - Jornada 7 (Viernes Noche)",
                "stadium": "Signal Iduna Park (Dortmund)",
                "spectators_est": "81,365 en estadio (~32M audiencia global)",
                "referee": "Sascha Stegemann",
                "referee_avg_yellows": 4.1,
                "referee_avg_reds": 0.16,
                "intensity": "Máxima (Signal Iduna Park encendido; Dortmund de Sahin con Guirassy buscando el asalto al liderato)"
            },
            ("Napoli", "Como"): {
                "tournament": "Serie A - Giornata 7 (Estelar de Viernes)",
                "stadium": "Stadio Diego Armando Maradona (Nápoles)",
                "spectators_est": "50,500 en estadio (~28M audiencia global)",
                "referee": "Ermanno Feliciani",
                "referee_avg_yellows": 4.2,
                "referee_avg_reds": 0.15,
                "intensity": "Muy Alta (Napoli de Antonio Conte liderando la Serie A con Kvaratskhelia, Lukaku y McTominay)"
            },
            ("Marseille", "Angers"): {
                "tournament": "Ligue 1 McDonald's - Jornada 7 (Viernes)",
                "stadium": "Orange Vélodrome (Marsella)",
                "spectators_est": "64,000 en estadio (~22M audiencia global)",
                "referee": "Romain Lissorgue",
                "referee_avg_yellows": 3.9,
                "referee_avg_reds": 0.20,
                "intensity": "Alta (El Vélodrome rugiendo con De Zerbi y Greenwood en busca de puntos clave de Champions)"
            },
            ("Leganés", "Valencia"): {
                "tournament": "LaLiga EA Sports - Jornada 9 (Viernes)",
                "stadium": "Estadio Municipal Butarque (Leganés, Madrid)",
                "spectators_est": "12,450 en estadio (~18M audiencia global)",
                "referee": "Jorge Figueroa Vázquez",
                "referee_avg_yellows": 4.7,
                "referee_avg_reds": 0.24,
                "intensity": "Tensión Extrema (Duelo directo por la permanencia con defensas cerradas y alto roce físico)"
            },
            ("Sunderland", "Leeds United"): {
                "tournament": "EFL Championship - Matchday 9 (Viernes Estelar)",
                "stadium": "Stadium of Light (Sunderland)",
                "spectators_est": "41,500 en estadio (~14M audiencia global)",
                "referee": "Tim Robinson",
                "referee_avg_yellows": 3.8,
                "referee_avg_reds": 0.12,
                "intensity": "Máxima (Batalla por el ascenso directo a Premier League en un Stadium of Light a reventar)"
            },
            ("Rio Ave", "Famalicão"): {
                "tournament": "Liga Portugal Betclic - Jornada 8 (Viernes)",
                "stadium": "Estádio dos Arcos (Vila do Conde)",
                "spectators_est": "5,300 en estadio (~4M audiencia global)",
                "referee": "Gustavo Correia",
                "referee_avg_yellows": 5.4,
                "referee_avg_reds": 0.28,
                "intensity": "Alta (Duelo táctico portugués con alta fricción y arbitraje severo)"
            },
"""

marker_ctx = "        return matches.get((home_team, away_team), {"
if "Borussia Dortmund\", \"St. Pauli" not in code:
    code = code.replace(marker_ctx, friday_contexts + "\n" + marker_ctx)

with open(agent_file, "w", encoding="utf-8") as f:
    f.write(code)

print("DataScoutAgent enriquecido con éxito con los 6 partidos del VIERNES!")
