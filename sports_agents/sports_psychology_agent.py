"""
SportsPsychologyAgent:
Agente analista de factores psicológicos, clima emocional del vestuario,
índice de urgencia competitiva, hostilidad ambiental (Factor Caldera) y complacencia.
"""

from typing import Dict, Any


class SportsPsychologyAgent:
    def __init__(self):
        self.name = "SportsPsychologyAgent"

    def analyze_emotional_context(self, home_team: str, away_team: str, tournament: str) -> Dict[str, Any]:
        """
        Calcula índices psicológicos que condicionan el resultado del partido.
        """
        # 1. Índice de Urgencia Competitiva (0.0 a 1.0)
        is_friendly = "Amistoso" in tournament or "Kirin" in tournament
        urgency_index = 0.40 if is_friendly else 0.90

        # 2. Factor Caldera / Hostilidad del Estadio (0.0 a 1.0)
        intimidation_ratings = {
            "Alemania": {"stadium": "Signal Iduna Park (Dortmund)", "intimidation": 0.92, "impact": "Presión asfixiante para el rival"},
            "Irlanda": {"stadium": "Aviva Stadium (Dublín)", "intimidation": 0.88, "impact": "Hinchada ruidosa, balones aéreos jaleados, juego muy físico"},
            "Gales": {"stadium": "Cardiff City Stadium", "intimidation": 0.82, "impact": "Sentido de pertenencia nacional fuerte"},
            "Grecia": {"stadium": "OPAP Arena (Atenas)", "intimidation": 0.85, "impact": "Ambiente hostil mediterráneo"},
            "Dinamarca": {"stadium": "Parken Stadium (Copenhague)", "intimidation": 0.78, "impact": "Muralla roja ordenada"},
            "Japón": {"stadium": "Estadio Nacional (Tokio)", "intimidation": 0.40, "impact": "Ambiente festivo, respetuoso, poco intimidante"}
        }

        stadium_info = intimidation_ratings.get(home_team, {"stadium": "Estadio Neutral", "intimidation": 0.50, "impact": "Neutro"})

        # 3. Regla del Suelo de Empate (Draw Floor Protection)
        # En selecciones europeas / competitivas, el empate de visita NUNCA debe bajar de 26%
        min_draw_floor_pct = 26.0 if not is_friendly else 24.0

        # 4. Complacencia por Goleada (Anti-Córner trigger)
        complacency_risk = "Alto" if home_team in ["España", "Alemania", "Portugal"] else "Medio"

        return {
            "tournament_urgency": urgency_index,
            "is_friendly": is_friendly,
            "stadium_name": stadium_info["stadium"],
            "intimidation_factor": stadium_info["intimidation"],
            "intimidation_impact": stadium_info["impact"],
            "minimum_draw_floor_pct": min_draw_floor_pct,
            "complacency_risk": complacency_risk,
            "psychological_notes": f"Urgencia: {'Baja (Amistoso)' if is_friendly else 'Máxima (Puntos Oficiales)'} | Caldera: {stadium_info['intimidation'] * 100}%"
        }
