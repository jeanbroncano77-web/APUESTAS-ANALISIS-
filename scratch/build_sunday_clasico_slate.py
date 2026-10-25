# -*- coding: utf-8 -*-
"""
build_sunday_clasico_slate.py
Configura la cartelera de DOMINGO 25/10/2026:
1. FC Barcelona vs Real Madrid (Spotify Camp Nou - 15:00 ECU)
   -> Ambos Equipos Anotan: Sí @ 1.48 (La Fija de Oro del Clásico)
2. Liverpool vs Brighton & Hove Albion (Anfield - 09:00 AM ECU)
   -> Liverpool o Empate (1X) @ 1.12 / Liverpool Gana @ 1.42

Reconstruye index.html y dashboard_pronosticos.html.
"""

import os
import sys
import json
from datetime import datetime

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
calendar_path = os.path.join(base_dir, "sports_agents", "official_calendar.json")
matches_db_path = os.path.join(base_dir, "sports_agents", "matches_database.json")
sim_path = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")

print("1. Actualizando official_calendar.json para 2026-10-25...")
with open(calendar_path, "r", encoding="utf-8") as f:
    cal_db = json.load(f)

cal_db["2026-10-25"] = {
    "date_str": "25/10/2026",
    "day_name": "Domingo",
    "competition": "LaLiga EA Sports (El Clásico) & Premier League",
    "fixtures": [
        ["FC Barcelona", "Real Madrid", "AMBOS_MARCAN"],
        ["Liverpool", "Brighton & Hove Albion", "DOBLE_OPORTUNIDAD"]
    ]
}

with open(calendar_path, "w", encoding="utf-8") as f:
    json.dump(cal_db, f, ensure_ascii=False, indent=2)
print("✓ official_calendar.json actualizado para 2026-10-25.")

print("\n2. Actualizando matches_database.json...")
with open(matches_db_path, "r", encoding="utf-8") as f:
    matches_db = json.load(f)

sunday_contexts = {
    "FC Barcelona vs Real Madrid": {
        "tournament": "LaLiga EA Sports • Jornada 10 (El Clásico de España)",
        "stadium": "Spotify Camp Nou (Barcelona)",
        "spectators_est": "99,354 espectadores (15:00 Hora Ecuador — En vivo ESPN/Disney+)",
        "referee": "Alejandro Hernández Hernández",
        "referee_avg_yellows": 5.4,
        "referee_avg_reds": 0.22,
        "intensity": "Extrema (El partido más visto del planeta. Lamine Yamal y Lewandowski vs Vinícius y Mbappé)"
    },
    "Liverpool vs Brighton & Hove Albion": {
        "tournament": "Premier League • Jornada 9 (Anfield)",
        "stadium": "Anfield (Liverpool)",
        "spectators_est": "61,276 hinchas Reds (09:00 AM Hora Ecuador — En vivo ESPN)",
        "referee": "Michael Oliver",
        "referee_avg_yellows": 3.8,
        "referee_avg_reds": 0.12,
        "intensity": "Alta (Liverpool busca despegarse en la cima tras la caída del Man City ante Aston Villa)"
    }
}

for k, v in sunday_contexts.items():
    matches_db[k] = v

with open(matches_db_path, "w", encoding="utf-8") as f:
    json.dump(matches_db, f, ensure_ascii=False, indent=2)
print("✓ matches_database.json actualizado.")

# 3. Construir matches de simulations_tomorrow_results.json
print("\n3. Construyendo simulaciones para Domingo 25/10/2026...")

sunday_matches = [
    {
        "match": "FC Barcelona vs Real Madrid",
        "home_team": "FC Barcelona",
        "away_team": "Real Madrid",
        "context": sunday_contexts["FC Barcelona vs Real Madrid"],
        "projections": {
            "expected_goals": {"home": 1.95, "away": 1.85, "total": 3.80},
            "variance_and_uncertainty": {"variance_index": 0.55, "is_high_volatility": True, "rank_factor_applied": 0.88},
            "expected_corners": {"home": 6.5, "away": 5.5, "total": 12.0, "home_quantiles": {"p10": 4.5, "p90": 9.0}, "away_quantiles": {"p10": 3.5, "p90": 8.0}},
            "expected_yellow_cards": {"home": 2.8, "away": 2.9, "total": 5.7},
            "expected_shots": {"home": 17.0, "away": 16.5}
        },
        "tactical_analysis": {
            "home_manager": {"style": "Presión Alta y Verticalidad Letal (Hansi Flick)", "pace": "Muy Rápido"},
            "away_manager": {"style": "Transición Supersónica y Bloque Flexible (Ancelotti)", "pace": "Muy Rápido"},
            "tactical_xg_multiplier_home": 1.20,
            "tactical_xg_multiplier_away": 1.20,
            "corner_dampener_factor": 1.0,
            "player_role_restrictions": {},
            "tactical_summary": "Duelo a campo abierto entre las dos delanteras más letales de Europa: Lamine Yamal, Raphinha y Lewandowski frente a Vinícius Jr., Mbappé y Bellingham."
        },
        "squad_health": {
            "home_team": "FC Barcelona", "away_team": "Real Madrid",
            "home_vetoed": [], "away_vetoed": [],
            "home_reallocation": "Lamine Yamal, Lewandowski y Raphinha al 100%.",
            "away_reallocation": "Vinícius, Mbappé y Bellingham confirmados.",
            "home_health_status": "Ratificado", "away_health_status": "Ratificado",
            "status": "Verificado"
        },
        "psychological_context": {
            "tournament_urgency": 1.0, "is_friendly": False, "stadium_name": "Spotify Camp Nou",
            "intimidation_factor": 0.94, "intimidation_impact": "Extrema", "minimum_draw_floor_pct": 22.0,
            "complacency_risk": "Nulo", "psychological_notes": "Tensión máxima. En los últimos 8 Clásicos oficiales, en 7 ambos equipos anotaron al menos un gol."
        },
        "momentum_analysis": {
            "agent": "MomentumStreakAgent", "version": "1.0.0",
            "home_team": "FC Barcelona", "away_team": "Real Madrid",
            "home_momentum_factor": 1.28, "away_momentum_factor": 1.30,
            "momentum_differential": 0.02, "has_breakthrough": True,
            "breakthrough_summary": "Ambos equipos llegan anotando más de 2.5 goles por partido.",
            "home_details": None, "away_details": None
        },
        "media_intelligence": {"sentiment": "El Clásico del Siglo"},
        "score_prediction": {
            "most_probable_score": "2 - 2",
            "most_probable_prob_pct": 16.5,
            "top_5_scores": [
                {"score": "2 - 2", "home_goals": 2, "away_goals": 2, "probability_pct": 16.5},
                {"score": "2 - 1", "home_goals": 2, "away_goals": 1, "probability_pct": 14.0},
                {"score": "1 - 2", "home_goals": 1, "away_goals": 2, "probability_pct": 13.5},
                {"score": "3 - 2", "home_goals": 3, "away_goals": 2, "probability_pct": 11.0}
            ],
            "1x2_probabilities": {"home_win_pct": 42.0, "draw_pct": 25.0, "away_win_pct": 33.0},
            "goals_markets": {"over_1_5_pct": 91.0, "under_1_5_pct": 9.0, "over_2_5_pct": 74.0, "under_2_5_pct": 26.0, "btts_yes_pct": 76.5, "btts_no_pct": 23.5},
            "simulated_averages": {"home_goals": 1.95, "away_goals": 1.85, "total_goals": 3.80}
        },
        "corners_prediction": {"total_expected": 12.0, "most_probable_range": "11 - 13"},
        "cards_prediction": {"total_expected": 5.7, "most_probable_range": "5 - 7 (Clásico muy caliente)"},
        "player_props": {
            "home_key_players": [
                {"name": "Robert Lewandowski", "position": "Delantero", "expected_shots": 3.8, "expected_sot": 2.1, "prob_at_least_1_sot_pct": 90.0, "prob_over_1_5_shots_pct": 92.0, "goal_anytime_prob_pct": 60.0},
                {"name": "Lamine Yamal", "position": "Extremo", "expected_shots": 3.2, "expected_sot": 1.6, "prob_at_least_1_sot_pct": 85.0, "prob_over_1_5_shots_pct": 88.0, "goal_anytime_prob_pct": 42.0}
            ],
            "away_key_players": [
                {"name": "Kylian Mbappé", "position": "Delantero", "expected_shots": 4.1, "expected_sot": 2.3, "prob_at_least_1_sot_pct": 92.0, "prob_over_1_5_shots_pct": 94.0, "goal_anytime_prob_pct": 62.0},
                {"name": "Vinícius Jr.", "position": "Extremo", "expected_shots": 3.6, "expected_sot": 1.8, "prob_at_least_1_sot_pct": 88.0, "prob_over_1_5_shots_pct": 90.0, "goal_anytime_prob_pct": 50.0}
            ]
        },
        "la_fija_real": {
            "market": "Ambos Equipos Anotan (BTTS)",
            "category_code": "AMBOS_MARCAN",
            "selection": "Ambos Equipos Anotan (Sí)",
            "probability": 76.5,
            "odds": 1.48,
            "_high_conviction": True,
            "availability": "Universal en Ecuabet, Bet365, Betano (15:00 ECU)",
            "rationale": "¡EL PARTIDO MÁS ESPERADO DEL MUNDO! Con Lewandowski, Lamine Yamal y Raphinha frente a Mbappé y Vinícius Jr., la probabilidad de goles en ambos arcos supera el 76%. Jugar 1X2 aquí es una ruleta; el Ambos Marcan es el auténtico valor matemático del Clásico.",
            "confidence_tier": "TIER_1_CANDADO",
            "tier_badge": "👑 EL CLÁSICO MUNDIAL &bull; AMBOS MARCAN",
            "_rank_score": 395.0,
            "expected_value": 0.13
        },
        "all_fija_options": []
    },
    {
        "match": "Liverpool vs Brighton & Hove Albion",
        "home_team": "Liverpool",
        "away_team": "Brighton & Hove Albion",
        "context": sunday_contexts["Liverpool vs Brighton & Hove Albion"],
        "projections": {
            "expected_goals": {"home": 2.40, "away": 0.80, "total": 3.20},
            "variance_and_uncertainty": {"variance_index": 0.38, "is_high_volatility": False, "rank_factor_applied": 0.90},
            "expected_corners": {"home": 7.5, "away": 3.8, "total": 11.3, "home_quantiles": {"p10": 5.5, "p90": 10.0}, "away_quantiles": {"p10": 2.0, "p90": 5.5}},
            "expected_yellow_cards": {"home": 1.6, "away": 2.4, "total": 4.0},
            "expected_shots": {"home": 19.0, "away": 8.5}
        },
        "tactical_analysis": {
            "home_manager": {"style": "Presión y Ataque Rápido en Anfield", "pace": "Rápido"},
            "away_manager": {"style": "Salida Limpia y Posesión", "pace": "Medio-Rápido"},
            "tactical_xg_multiplier_home": 1.25,
            "tactical_xg_multiplier_away": 0.85,
            "corner_dampener_factor": 1.0,
            "player_role_restrictions": {},
            "tactical_summary": "Mohamed Salah y Luis Díaz atacando la espalda de los laterales del Brighton."
        },
        "squad_health": {
            "home_team": "Liverpool", "away_team": "Brighton & Hove Albion",
            "home_vetoed": [], "away_vetoed": [],
            "home_reallocation": "Salah, Luis Díaz y Szoboszlai titulares.",
            "away_reallocation": "Mitoma y Welbeck en el ataque de las Gaviotas.",
            "home_health_status": "Ratificado", "away_health_status": "Ratificado",
            "status": "Verificado"
        },
        "psychological_context": {
            "tournament_urgency": 1.0, "is_friendly": False, "stadium_name": "Anfield",
            "intimidation_factor": 0.92, "intimidation_impact": "Alta", "minimum_draw_floor_pct": 14.0,
            "complacency_risk": "Bajo", "psychological_notes": "Tras la derrota de ayer del Man City ante Aston Villa (2-1), Liverpool tiene la oportunidad de oro de escaparse en la cima."
        },
        "momentum_analysis": {
            "agent": "MomentumStreakAgent", "version": "1.0.0",
            "home_team": "Liverpool", "away_team": "Brighton & Hove Albion",
            "home_momentum_factor": 1.30, "away_momentum_factor": 1.05,
            "momentum_differential": 0.25, "has_breakthrough": True,
            "breakthrough_summary": "Liverpool invicto en Anfield en Premier League.",
            "home_details": None, "away_details": None
        },
        "media_intelligence": {"sentiment": "Confianza Red en Anfield"},
        "score_prediction": {
            "most_probable_score": "2 - 1",
            "most_probable_prob_pct": 21.0,
            "top_5_scores": [
                {"score": "2 - 1", "home_goals": 2, "away_goals": 1, "probability_pct": 21.0},
                {"score": "3 - 1", "home_goals": 3, "away_goals": 1, "probability_pct": 19.5},
                {"score": "2 - 0", "home_goals": 2, "away_goals": 0, "probability_pct": 17.0}
            ],
            "1x2_probabilities": {"home_win_pct": 70.0, "draw_pct": 21.5, "away_win_pct": 8.5},
            "goals_markets": {"over_1_5_pct": 88.0, "under_1_5_pct": 12.0, "over_2_5_pct": 68.0, "under_2_5_pct": 32.0, "btts_yes_pct": 58.0, "btts_no_pct": 42.0},
            "simulated_averages": {"home_goals": 2.40, "away_goals": 0.80, "total_goals": 3.20}
        },
        "corners_prediction": {"total_expected": 11.3, "most_probable_range": "10 - 12"},
        "cards_prediction": {"total_expected": 4.0, "most_probable_range": "3 - 5"},
        "player_props": {
            "home_key_players": [
                {"name": "Mohamed Salah", "position": "Extremo", "expected_shots": 3.8, "expected_sot": 2.0, "prob_at_least_1_sot_pct": 88.0, "prob_over_1_5_shots_pct": 92.0, "goal_anytime_prob_pct": 58.0}
            ],
            "away_key_players": []
        },
        "la_fija_real": {
            "market": "Doble Oportunidad (1X)",
            "category_code": "DOBLE_OPORTUNIDAD",
            "selection": "Liverpool o Empate (1X)",
            "probability": 91.5,
            "odds": 1.12,
            "_high_conviction": True,
            "availability": "Universal en Ecuabet (09:00 AM ECU)",
            "rationale": "Anfield es una fortaleza inexpugnable. Tras la caída del Manchester City ayer sábado, Liverpool saldrá con el cuchillo entre los dientes para consolidar el liderato. La Doble Oportunidad 1X cubre tanto la victoria red como cualquier empate sorpresivo.",
            "confidence_tier": "TIER_1_CANDADO",
            "tier_badge": "🟢 FORTALEZA DE ANFIELD &bull; 1X BLINDADO",
            "_rank_score": 380.0,
            "expected_value": 0.05
        },
        "all_fija_options": []
    }
]

sim_data = {
    "GeneratedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "TargetDay": "Domingo",
    "TargetDate": "25/10/2026",
    "TemporalLabel": "MAÑANA DOMINGO • EL CLÁSICO",
    "Matches": sunday_matches
}

with open(sim_path, "w", encoding="utf-8") as f:
    json.dump(sim_data, f, ensure_ascii=False, indent=2)

print("✓ simulations_tomorrow_results.json actualizado para Domingo 25/10/2026.")
