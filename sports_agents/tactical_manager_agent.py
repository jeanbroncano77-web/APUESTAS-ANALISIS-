"""
TacticalManagerAgent:
Agente analista de directores técnicos, pizarrón táctico,
choque de estilos y dinámica del marcador (Game State).
"""

from typing import Dict, Any


class TacticalManagerAgent:
    def __init__(self):
        self.name = "TacticalManagerAgent"
        
        self.manager_profiles = {
            "Alemania": {"manager": "Julian Nagelsmann", "style": "Posesión vertical / Contrapresión", "pace": "Alto", "risk_tolerance": "Alta"},
            "Serbia": {"manager": "Dragan Stojkovic", "style": "Juego aéreo directo / 3-5-2 físico", "pace": "Medio-Bajo", "risk_tolerance": "Media"},
            "Portugal": {"manager": "Roberto Martínez", "style": "Apertura de bandas / Dominancia territorial", "pace": "Alto", "risk_tolerance": "Media-Alta"},
            "Dinamarca": {"manager": "Lars Knudsen (Interino)", "style": "Bloque compacto / Transición organizada", "pace": "Medio", "risk_tolerance": "Baja"},
            "Países Bajos": {"manager": "Ronald Koeman", "style": "4-3-3 pragmático de visita / Gestión de ritmo", "pace": "Medio", "risk_tolerance": "Baja"},
            "Grecia": {"manager": "Ivan Jovanovic", "style": "Bloque bajo 5-3-2 / Embudo defensivo", "pace": "Muy Bajo", "risk_tolerance": "Nula"},
            "Noruega": {"manager": "Stale Solbakken", "style": "Transición vertical rápida / Balón a Haaland", "pace": "Alto en contragolpe", "risk_tolerance": "Alta"},
            "Gales": {"manager": "Craig Bellamy", "style": "Alta intensidad y repliegue / Propenso a errores en salida", "pace": "Medio-Alto", "risk_tolerance": "Media"},
            "Austria": {"manager": "Ralf Rangnick", "style": "Gegenpressing agresivo / Vulnerable a juego directo", "pace": "Muy Alto", "risk_tolerance": "Alta"},
            "Irlanda": {"manager": "Heimir Hallgrimsson", "style": "Fútbol directo británico / Balón largo al 9", "pace": "Físico / Interrumpido", "risk_tolerance": "Baja"},
            "Japón": {"manager": "Hajime Moriyasu", "style": "Presión organizada / Rotación masiva en amistosos", "pace": "Interrumpido en 2T", "risk_tolerance": "Media"},
            "Ecuador": {"manager": "Sebastián Beccacece", "style": "Orden táctico / Bloque rocoso de visita", "pace": "Bajo", "risk_tolerance": "Baja"}
        }

    def evaluate_tactical_matchup(self, home_team: str, away_team: str, lambda_h: float, lambda_a: float) -> Dict[str, Any]:
        """
        Evalúa el choque táctico de entrenadores y genera modificadores
        para goles, córners y minutos de figuras.
        """
        h_mgr = self.manager_profiles.get(home_team, {"style": "Estándar", "pace": "Medio"})
        a_mgr = self.manager_profiles.get(away_team, {"style": "Estándar", "pace": "Medio"})

        xg_modifier_home = 1.0
        xg_modifier_away = 1.0
        corner_dampener = 1.0
        substitution_risk = {}

        # 1. Choque contra Bloque Bajo (Caso Grecia vs Países Bajos)
        if away_team == "Países Bajos" and home_team == "Grecia":
            # El 5-3-2 griego asfixia el ataque central
            xg_modifier_away = 0.85
            xg_modifier_home = 0.70
            substitution_risk["Xavi Simons"] = {
                "expected_minutes": 62,
                "role_restriction": "Extremo fijador pegado a la banda; pocas incursiones de remate al área.",
                "sot_probability_reduction": 0.35  # Reduce drásticamente la probabilidad de tiro a puerta
            }

        # 2. Choque Gegenpressing vs Juego Directo (Caso Irlanda vs Austria)
        if away_team == "Austria" and home_team == "Irlanda":
            # Irlanda saltea el pressing de Rangnick con pelotazos directos
            xg_modifier_away = 0.80  # Austria pierde efectividad de contragolpe
            xg_modifier_home = 1.10  # Irlanda gana segundas jugadas aéreas

        # 3. Choque Amistoso de Rotaciones Masivas (Caso Japón vs Ecuador)
        if home_team == "Japón" and away_team == "Ecuador":
            # 6 sustituciones en segundo tiempo cortan el ritmo de gol
            xg_modifier_home = 0.75
            xg_modifier_away = 0.75
            corner_dampener = 0.80

        # 4. Asimetría de Superestrella (Gales vs Noruega)
        if away_team == "Noruega":
            # Haaland convierte ocasiones de bajo xG en goles
            xg_modifier_away = 1.25

        # 5. Game-State Dampener para Córners (Caso España o partidos desiguales)
        if abs(lambda_h - lambda_a) >= 1.4:
            # Si un equipo es infinitamente superior y golea temprano, en el segundo tiempo los córners bajan
            corner_dampener *= 0.85

        return {
            "home_manager": h_mgr,
            "away_manager": a_mgr,
            "tactical_xg_multiplier_home": round(xg_modifier_home, 3),
            "tactical_xg_multiplier_away": round(xg_modifier_away, 3),
            "corner_dampener_factor": round(corner_dampener, 3),
            "player_role_restrictions": substitution_risk,
            "tactical_summary": f"Choque de estilos: {h_mgr['style']} vs {a_mgr['style']}"
        }
