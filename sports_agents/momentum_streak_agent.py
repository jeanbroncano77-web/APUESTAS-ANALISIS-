"""
sports_agents/momentum_streak_agent.py
---------------------------------------
Agente Especialista #11: Detector de Rachas de Quiebre, Inflexión y Dinámicas de Resurgimiento (Momentum & Inflection Agent).

Misión:
Identificar equipos que experimentan un cambio drástico de paradigma competitivo (inflexión),
rompiendo rachas históricas negativas o entrando en rachas triunfales exponenciales que los
modelos estadísticos tradicionales (basados en 2-3 años de historia) tardan demasiado en reconocer.

Caso Emblemático:
La Selección de Grecia bajo Ivan Jovanović: tras años de declive futbolístico, derrotas y ausencia
de grandes torneos, experimenta una metamorfosis táctica y anímica logrando victorias contundentes,
incluyendo la victoria histórica en Wembley 1-2 ante Inglaterra y racha consecutiva de victorias.
"""

from typing import Dict, Any, List
import math


class MomentumStreakAgent:
    def __init__(self):
        self.name = "MomentumStreakAgent"
        self.version = "1.0.0"
        
        # Base de conocimiento curada de equipos con puntos de inflexión y rachas activas
        self.inflection_database = {
            "Grecia": {
                "status": "RESURGIMIENTO_HISTORICO",
                "inflection_factor": 1.42, # Impulso del +42% sobre su xG base histórico
                "recent_form": ["W", "W", "W", "W", "W"],
                "recent_goals_scored": 11,
                "recent_goals_conceded": 1,
                "clean_sheets_pct": 80.0,
                "key_driver": "Metamorfosis con Ivan Jovanović, cohesión anímica máxima y voracidad ofensiva (Pavlidis / Bakasetas).",
                "historical_bias_correction": "Los modelos tradicionales le asignaban 12% de chance ante gigantes; su racha real eleva su competitividad efectiva a >45%.",
                "market_inefficiency_edge": "+18.4% de valor sobre cuotas de casas de apuestas que subestiman su racha."
            },
            "España": {
                "status": "RACHA_IMPERIAL_POST_EURO",
                "inflection_factor": 1.25,
                "recent_form": ["W", "W", "W", "D", "W"],
                "recent_goals_scored": 14,
                "recent_goals_conceded": 3,
                "clean_sheets_pct": 60.0,
                "key_driver": "Generación dorada Lamine Yamal / Nico Williams con automatismos ofensivos imparables.",
                "historical_bias_correction": "xG ofensivo sostenido superior a 2.3 por partido.",
                "market_inefficiency_edge": "+8.2% de valor en Over 1.5 goles de equipo."
            },
            "Noruega": {
                "status": "INFLEXION_OFENSIVA",
                "inflection_factor": 1.18,
                "recent_form": ["W", "D", "W", "W", "L"],
                "recent_goals_scored": 10,
                "recent_goals_conceded": 4,
                "clean_sheets_pct": 40.0,
                "key_driver": "Conexión Haaland + Sorloth con generación superior a 15 disparos totales por encuentro.",
                "historical_bias_correction": "Remates de Haaland consistentemente por encima de la línea Over 2.5 real.",
                "market_inefficiency_edge": "+12.1% en mercados de goles totales y hándicap asiático."
            },
            "Austria": {
                "status": "PRENSADO_RANGNICK_SOLIDO",
                "inflection_factor": 1.15,
                "recent_form": ["W", "D", "W", "L", "W"],
                "recent_goals_scored": 9,
                "recent_goals_conceded": 4,
                "clean_sheets_pct": 50.0,
                "key_driver": "Gegenpressing de Ralf Rangnick con recuperación en tercio ofensivo.",
                "historical_bias_correction": "Equipos defensivos sufren alta tasa de conceder 8+ córners ante su asedio.",
                "market_inefficiency_edge": "+9.5% en córners a favor de Austria."
            }
        }
        
        self.tier1_giants = {
            "Alemania", "Francia", "España", "Inglaterra", "Portugal", "Países Bajos",
            "Argentina", "Brasil", "Real Madrid", "Bayern Munich", "Manchester City", "Barcelona"
        }

    def analyze_match_momentum(self, home_team: str, away_team: str) -> Dict[str, Any]:
        """
        Calcula el impacto de momentum, rachas y puntos de inflexión para un enfrentamiento.
        Ajusta expectativas de goles y factores de ventaja de racha.
        Aplica un freno de realismo (Tier-1 Dampener) si el rival es un coloso europeo.
        """
        home_info = self.inflection_database.get(home_team, None)
        away_info = self.inflection_database.get(away_team, None)

        home_factor = home_info["inflection_factor"] if home_info else 1.0
        away_factor = away_info["inflection_factor"] if away_info else 1.0

        # FRENO TIER-1 (Lección de Grecia vs Alemania):
        # Si un equipo en racha enfrenta a una superpotencia mundial, su impulso anímico se neutraliza en un 75%
        # ante la asfixia táctica y jerarquía individual del gigante.
        dampener_applied = []
        if home_info and away_team in self.tier1_giants:
            old_h = home_factor
            home_factor = round(1.0 + (home_factor - 1.0) * 0.25, 2)
            dampener_applied.append(f"Freno Tier-1 en {home_team}: {old_h}x -> {home_factor}x ante coloso {away_team}")

        if away_info and home_team in self.tier1_giants:
            old_a = away_factor
            away_factor = round(1.0 + (away_factor - 1.0) * 0.25, 2)
            dampener_applied.append(f"Freno Tier-1 en {away_team}: {old_a}x -> {away_factor}x ante coloso {home_team}")

        # Análisis diferencial
        momentum_differential = home_factor - away_factor
        
        has_breakthrough_team = False
        breakthrough_details = []

        if home_info and home_info["status"] == "RESURGIMIENTO_HISTORICO":
            has_breakthrough_team = True
            breakthrough_details.append(f"🟢 {home_team}: {home_info['key_driver']} (Factor Inflexión: {home_factor}x)")

        if away_info and away_info["status"] == "RESURGIMIENTO_HISTORICO":
            has_breakthrough_team = True
            breakthrough_details.append(f"🟢 {away_team}: {away_info['key_driver']} (Factor Inflexión: {away_factor}x)")

        if dampener_applied:
            breakthrough_details.extend([f"🛡️ {d}" for d in dampener_applied])

        # Ajuste probabilístico para compensar el retraso de modelos estacionarios (TimesFM baseline)
        return {
            "agent": self.name,
            "version": self.version,
            "home_team": home_team,
            "away_team": away_team,
            "home_momentum_factor": home_factor,
            "away_momentum_factor": away_factor,
            "momentum_differential": round(momentum_differential, 3),
            "has_breakthrough": has_breakthrough_team,
            "breakthrough_summary": " | ".join(breakthrough_details) if breakthrough_details else "Ambos equipos en rangos estándar de volatilidad.",
            "home_details": home_info,
            "away_details": away_info,
            "tier1_dampener_active": bool(dampener_applied),
            "recommendation_bias": (
                f"IMPULSAR_POSITIVAMENTE a {home_team if home_factor > away_factor else away_team}"
                if abs(momentum_differential) >= 0.15 else "MANTENER_EQUILIBRIO"
            )
        }


if __name__ == "__main__":
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding='utf-8')
    agent = MomentumStreakAgent()
    res = agent.analyze_match_momentum("Grecia", "Países Bajos")
    print("=== TEST MOMENTUM STREAK AGENT ===")
    print(f"Partido: {res['home_team']} vs {res['away_team']}")
    print(f"Inflexión detectada: {res['has_breakthrough']}")
    print(f"Resumen: {res['breakthrough_summary']}")
    print(f"Recomendación: {res['recommendation_bias']}")
