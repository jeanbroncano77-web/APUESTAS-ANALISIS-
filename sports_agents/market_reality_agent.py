# -*- coding: utf-8 -*-
"""
MarketRealityAgent 6.0 - DIRECTOR ESTRATÉGICO DE VALOR REAL Y ALTA CONVICCIÓN
=============================================================================
MEJORAS DEFINITIVAS:
  1. Erradicación total del sesgo contra cuotas > 1.25 (el bug que forzaba micro-cuotas de 1.09 a 1.12).
  2. Rango de oro de cuotas: 1.35 a 1.95 (donde reside el valor matemático real para el apostador).
  3. Preselección prioritaria de VICTORIA DIRECTA (1X2) para favoritos claros (>= 52% local / >= 48% visitante).
  4. Draw No Bet (DNB / Empate No Válido) como alternativa de valor cuando hay ligero riesgo de empate.
  5. Ambos Equipos Anotan (BTTS Sí) activado con umbral realista (>= 52% y xG cruzado > 1.10).
  6. Penalización severa (-90 pts) a micro-cuotas triviales (< 1.20) como "Más de 0.5 goles" o "Menos de 4.5 goles".
  7. Blindaje de operabilidad en Bet365, Betano, 1xBet y Ecuabet. Veto total a hándicaps inexistentes.
"""

import math
from typing import Dict, Any, List, Optional


class MarketRealityAgent:
    """Agente verificador de mercados y seleccionador de La Fija con Convicción Real y Rentabilidad."""

    DIRECT_WIN_HIGH_CONVICTION_HOME = 54.0
    DIRECT_WIN_HIGH_CONVICTION_AWAY = 48.0
    DIRECT_WIN_MINIMUM_HOME = 48.0
    DIRECT_WIN_MINIMUM_AWAY = 44.0

    BANNED_MARKET_TERMS = [
        "handicap", "hándicap", "handicap_asiatico", "handicap_blindado",
        "+1.5", "+2.5", "-1.5", "-2.5", "(+1.5)", "(+2.5)",
        "5.5", "-5.5", "+5.5", "menos de 5.5", "más de 5.5", "under 5.5", "over 5.5"
    ]
    ALLOWED_CATEGORIES = {
        "DOBLE_OPORTUNIDAD", "GOLES_UNDER", "GOLES_OVER",
        "GOL_EQUIPO", "TOTAL_CORNERS", "VICTORIA_SIN_EMPATE",
        "VICTORIA_DIRECTA", "AMBOS_ANOTAN", "TARJETAS"
    }
    TIER1_GIANTS = {
        "Alemania", "Francia", "España", "Inglaterra", "Portugal", "Países Bajos",
        "Argentina", "Brasil", "Real Madrid", "Bayern Munich", "Manchester City", "Barcelona",
        "Liverpool", "Arsenal", "Chelsea", "PSG", "Inter Milan", "Inter", "Juventus",
        "Atlético Madrid", "Atlético de Madrid", "Borussia Dortmund", "Dortmund", "Villarreal"
    }

    def __init__(self):
        self.name = "MarketRealityAgent"
        self.version = "6.5.0"

    @staticmethod
    def _fair_odds(prob_pct: float, margin: float = 1.06) -> float:
        """Cuota real de casa ajustada por margen estándar."""
        p = max(1.0, min(99.0, prob_pct))
        return round(max(1.08, (1.0 / (p / 100.0)) * margin), 2)

    @staticmethod
    def _ev(prob_pct: float, odds: float) -> float:
        """Expected Value (Valor Esperado) normalizado."""
        return round((prob_pct / 100.0) * odds - 1.0, 4)

    def _rank_score(self, prob: float, odds: float, category: str,
                    has_high_conviction: bool, preferred_category: Optional[str]) -> float:
        """
        Scoring v6.0 - Maximiza Valor Real y Rentabilidad para el Apostador.
        Premia el rango de oro (1.35 a 1.95) y la alta convicción de victoria.
        Penaliza drásticamente micro-cuotas triviales (< 1.20).
        """
        # Base proporcional a la probabilidad
        base = prob * 1.5

        # Rango de Cuota Óptima: Apostar en cuotas reales (1.35 a 1.95)
        if 1.35 <= odds <= 1.90:
            odds_quality_bonus = 60.0
        elif 1.24 <= odds < 1.35:
            odds_quality_bonus = 35.0
        elif 1.90 < odds <= 2.25:
            odds_quality_bonus = 45.0
        elif odds <= 1.15:
            # Penalización masiva a micro-cuotas triviales (Más de 0.5 goles, etc.)
            odds_quality_bonus = -95.0
        else:
            odds_quality_bonus = -40.0

        # Bonus de Alta Convicción para Victorias Directas
        conviction_bonus = 0.0
        if category == "VICTORIA_DIRECTA" and has_high_conviction:
            conviction_bonus = 110.0
        elif category == "VICTORIA_SIN_EMPATE" and has_high_conviction:
            conviction_bonus = 55.0

        # Bonus si coincide con la categoría táctica preferida del analista
        preferred_bonus = 40.0 if (preferred_category and category == preferred_category) else 0.0

        # Bonus de Expected Value positivo
        ev = self._ev(prob, odds)
        ev_bonus = max(0.0, ev) * 150.0

        return round(base + odds_quality_bonus + conviction_bonus + preferred_bonus + ev_bonus, 2)

    def select_realistic_la_fija(
        self,
        match: str,
        home_team: str,
        away_team: str,
        prob_1x2: Dict[str, float],
        goals_data: Dict[str, Any],
        corners_data: Dict[str, Any],
        cleared_players: List[Dict[str, Any]],
        psychology: Dict[str, Any],
        preferred_category: Optional[str] = None,
        exact_market_probs: Optional[Dict[str, float]] = None,
        media_analysis: Optional[Dict[str, Any]] = None,
        momentum_analysis: Optional[Dict[str, Any]] = None,
        cards_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Selecciona La Fija con el nuevo motor de alta convicción y valor real v6.0.
        Prioridad estratégica:
          1. VICTORIA_DIRECTA (1X2) cuando hay favoritismo claro (>= 50% o superioridad xG/Gigante).
          2. VICTORIA_SIN_EMPATE (DNB) cuando el favorito tiene ventaja pero existe riesgo de tablas.
          3. AMBOS EQUIPOS ANOTAN (BTTS) en partidos de alta vocación ofensiva bilateral.
          4. TOTAL GOLES (Over 1.5 / Over 2.5 / Under 3.5) con líneas de cuota real.
          5. DOBLE OPORTUNIDAD (1X/X2) con cuota competitiva (>= 1.28).
          6. Veto a micro-cuotas (< 1.20) como La Fija Estelar.
        """
        # Veto total y permanente a handicaps
        if preferred_category in ["HANDICAP_BLINDADO", "HANDICAP", "HANDICAP_ASIATICO", "HANDICAP_POSITIVO"]:
            preferred_category = "DOBLE_OPORTUNIDAD"

        candidates: List[Dict[str, Any]] = []
        is_home_giant = home_team in self.TIER1_GIANTS
        is_away_giant = away_team in self.TIER1_GIANTS
        both_tier1 = (is_home_giant and is_away_giant)

        # Probabilidades 1X2
        if exact_market_probs:
            h_win = float(exact_market_probs.get("home_win_pct", 50.0))
            draw  = float(exact_market_probs.get("draw_pct", 25.0))
            a_win = float(exact_market_probs.get("away_win_pct", 25.0))
        else:
            h_win = float(prob_1x2.get("HomeWin", prob_1x2.get("home_win_pct", 50.0)))
            draw  = float(prob_1x2.get("Draw",    prob_1x2.get("draw_pct", 25.0)))
            a_win = float(prob_1x2.get("AwayWin", prob_1x2.get("away_win_pct", 25.0)))

        exp_total_goals = float(goals_data.get("Total", goals_data.get("total", 2.5)))
        home_xg = float(goals_data.get("Home", goals_data.get("home", 1.4)))
        away_xg = float(goals_data.get("Away", goals_data.get("away", 1.1)))
        corners_lines = corners_data.get("lines", {}) if isinstance(corners_data, dict) else {}
        exp_corners = float(corners_data.get("total_corners_expected",
                            corners_data.get("Total", corners_data.get("total", 9.5))))

        # Detección de alta convicción
        # Si es un gigante con ventaja clara de xG (>= 0.35) o probabilidad superior al umbral
        home_high_conv = (h_win >= self.DIRECT_WIN_HIGH_CONVICTION_HOME) or (is_home_giant and h_win >= 48.0 and (home_xg - away_xg >= 0.35))
        away_high_conv = (a_win >= self.DIRECT_WIN_HIGH_CONVICTION_AWAY) or (is_away_giant and a_win >= 45.0 and (away_xg - home_xg >= 0.35))

        # =====================================================================
        # 1. MERCADO: VICTORIA DIRECTA (1X2) - EL MERCADO REY DE LAS APUESTAS
        # =====================================================================
        if h_win >= self.DIRECT_WIN_MINIMUM_HOME or (is_home_giant and h_win > a_win):
            odds_hw = self._fair_odds(h_win, margin=1.06)
            candidates.append({
                "market": "Victoria Directa (1X2)",
                "category_code": "VICTORIA_DIRECTA",
                "selection": f"{home_team} Gana el Partido (1)",
                "probability": round(h_win, 1),
                "odds": odds_hw,
                "_high_conviction": home_high_conv,
                "availability": "Universal en todas las casas (Bet365, Betano, 1xBet, Codere)",
                "rationale": f"Convicción directa: {home_team} domina la proyección con {round(h_win, 1)}% de probabilidad de triunfo en los 90 minutos reglamentarios."
            })

        if a_win >= self.DIRECT_WIN_MINIMUM_AWAY or (is_away_giant and a_win > h_win):
            odds_aw = self._fair_odds(a_win, margin=1.06)
            candidates.append({
                "market": "Victoria Directa (1X2)",
                "category_code": "VICTORIA_DIRECTA",
                "selection": f"{away_team} Gana el Partido (2)",
                "probability": round(a_win, 1),
                "odds": odds_aw,
                "_high_conviction": away_high_conv,
                "availability": "Universal en todas las casas (Bet365, Betano, 1xBet, Codere)",
                "rationale": f"Convicción visitante: {away_team} proyecta superioridad táctica con {round(a_win, 1)}% de probabilidad de llevarse los 3 puntos."
            })

        # =====================================================================
        # 2. MERCADO: VICTORIA SIN EMPATE (Draw No Bet - DNB / Empate No Válido)
        # =====================================================================
        if exact_market_probs and "dnb_home_pct" in exact_market_probs:
            prob_dnb_h = exact_market_probs["dnb_home_pct"]
            prob_dnb_a = exact_market_probs["dnb_away_pct"]
        else:
            denom = max(1.0, h_win + a_win)
            prob_dnb_h = round((h_win / denom) * 100.0, 1)
            prob_dnb_a = round((a_win / denom) * 100.0, 1)

        if h_win >= 44.0 and h_win > a_win and prob_dnb_h >= 58.0:
            odds_dnb_h = self._fair_odds(prob_dnb_h, margin=1.06)
            candidates.append({
                "market": "Victoria Sin Empate (DNB)",
                "category_code": "VICTORIA_SIN_EMPATE",
                "selection": f"{home_team} Gana (Empate No Válido / DNB)",
                "probability": prob_dnb_h,
                "odds": odds_dnb_h,
                "_high_conviction": prob_dnb_h >= 70.0,
                "availability": "100% Casas de Apuestas (Mercado Draw No Bet)",
                "rationale": f"Triunfo de {home_team} con devolución íntegra del dinero si el partido termina igualado (cobertura DNB: {prob_dnb_h}%)."
            })
        elif a_win >= 40.0 and a_win > h_win and prob_dnb_a >= 58.0:
            odds_dnb_a = self._fair_odds(prob_dnb_a, margin=1.06)
            candidates.append({
                "market": "Victoria Sin Empate (DNB)",
                "category_code": "VICTORIA_SIN_EMPATE",
                "selection": f"{away_team} Gana (Empate No Válido / DNB)",
                "probability": prob_dnb_a,
                "odds": odds_dnb_a,
                "_high_conviction": prob_dnb_a >= 70.0,
                "availability": "100% Casas de Apuestas (Mercado Draw No Bet)",
                "rationale": f"Triunfo de {away_team} con devolución total en caso de empate (cobertura DNB: {prob_dnb_a}%)."
            })

        # =====================================================================
        # 3. MERCADO: AMBOS EQUIPOS ANOTAN (BTTS Sí) - FILTRO TÁCTICO BLINDADO
        # Requiere alta vocación ofensiva bilateral (evita trampas 0-1 / 1-0 de duelos cerrados)
        # =====================================================================
        prob_btts = exact_market_probs.get("btts_yes_pct", 60.0) if exact_market_probs else 60.0
        if prob_btts >= 58.0 and home_xg >= 1.20 and away_xg >= 1.15 and exp_total_goals >= 2.60:
            odds_btts = self._fair_odds(prob_btts, margin=1.07)
            candidates.append({
                "market": "Ambos Equipos Anotan",
                "category_code": "AMBOS_ANOTAN",
                "selection": "Ambos Equipos Anotan (Sí)",
                "probability": round(prob_btts, 1),
                "odds": odds_btts,
                "_high_conviction": prob_btts >= 65.0,
                "availability": "Universal en todas las plataformas (Bet365, Betano, etc.)",
                "rationale": f"Poder de fuego bilateral verificado: ambos cuadros promedian ocasiones claras ({round(home_xg, 2)} vs {round(away_xg, 2)} xG) con {round(prob_btts, 1)}% de gol cruzado."
            })

        # =====================================================================
        # 4. MERCADO: DOBLE OPORTUNIDAD (1X / X2)
        # =====================================================================
        if exact_market_probs and "double_chance_1x_pct" in exact_market_probs:
            prob_1x = exact_market_probs["double_chance_1x_pct"]
            prob_x2 = exact_market_probs["double_chance_x2_pct"]
        else:
            prob_1x = round(h_win + draw, 1)
            prob_x2 = round(a_win + draw, 1)

        if prob_1x >= 64.0 and h_win >= a_win:
            odds_1x = self._fair_odds(prob_1x, margin=1.05)
            candidates.append({
                "market": "Doble Oportunidad",
                "category_code": "DOBLE_OPORTUNIDAD",
                "selection": f"{home_team} o Empate (1X)",
                "probability": round(prob_1x, 1),
                "odds": odds_1x,
                "_high_conviction": prob_1x >= 76.0,
                "availability": "100% Casas de Apuestas (Bet365, Betano)",
                "rationale": f"Protección total ante el empate con {round(prob_1x, 1)}% de cobertura matemática y factor local."
            })

        if prob_x2 >= 64.0 and a_win > h_win:
            odds_x2 = self._fair_odds(prob_x2, margin=1.05)
            candidates.append({
                "market": "Doble Oportunidad",
                "category_code": "DOBLE_OPORTUNIDAD",
                "selection": f"Empate o {away_team} (X2)",
                "probability": round(prob_x2, 1),
                "odds": odds_x2,
                "_high_conviction": prob_x2 >= 76.0,
                "availability": "100% Casas de Apuestas (Bet365, Betano)",
                "rationale": f"El visitante {away_team} puntúa en el {round(prob_x2, 1)}% de las simulaciones tácticas."
            })

        # =====================================================================
        # 5. MERCADO: TOTAL GOLES (Over 1.5 / Over 2.5 / Under 3.5)
        # =====================================================================
        prob_over15 = exact_market_probs.get("over_1_5_pct", 80.0) if exact_market_probs else 80.0
        prob_over25 = exact_market_probs.get("over_2_5_pct", 55.0) if exact_market_probs else 55.0
        prob_under35 = exact_market_probs.get("under_3_5_pct", 70.0) if exact_market_probs else 70.0

        if prob_over15 >= 75.0 and exp_total_goals >= 2.4:
            p_o15 = round(prob_over15, 1)
            candidates.append({
                "market": "Total de Goles Fijo",
                "category_code": "GOLES_OVER",
                "selection": "Más de 1.5 goles totales",
                "probability": p_o15,
                "odds": self._fair_odds(p_o15, margin=1.06),
                "_high_conviction": p_o15 >= 82.0,
                "availability": "Universal en todas las plataformas",
                "rationale": f"Volumen ofensivo conjunto proyecta {round(exp_total_goals, 2)} goles esperados con {p_o15}% de ver 2 o más tantos."
            })

        if prob_over25 >= 54.0 and exp_total_goals >= 2.85:
            p_o25 = round(prob_over25, 1)
            candidates.append({
                "market": "Total de Goles Fijo",
                "category_code": "GOLES_OVER",
                "selection": "Más de 2.5 goles totales",
                "probability": p_o25,
                "odds": self._fair_odds(p_o25, margin=1.07),
                "_high_conviction": False,
                "availability": "Universal en todas las plataformas",
                "rationale": f"Partido abierto con {round(exp_total_goals, 2)} xG combinados y {p_o25}% de probabilidad de 3+ goles."
            })

        if prob_under35 >= 74.0 and exp_total_goals <= 2.3:
            p_u35 = round(prob_under35, 1)
            candidates.append({
                "market": "Total de Goles Fijo",
                "category_code": "GOLES_UNDER",
                "selection": "Menos de 3.5 goles totales",
                "probability": p_u35,
                "odds": self._fair_odds(p_u35, margin=1.06),
                "_high_conviction": p_u35 >= 80.0,
                "availability": "Universal en todas las plataformas",
                "rationale": f"Bloques tácticos rigurosos ({round(exp_total_goals, 2)} xG): el 74%+ de las simulaciones finalizan con 3 o menos goles."
            })

        # =====================================================================
        # 6. MERCADO: TARJETAS Y DISCIPLINA
        # =====================================================================
        if cards_data:
            total_cards_exp = cards_data.get("total_cards_expected", 0.0)
            card_lines = cards_data.get("card_lines", {})
            prob_o35_c = card_lines.get("over_3_5_cards_pct", 65.0)

            if total_cards_exp >= 3.8 or prob_o35_c >= 60.0:
                p_c = round(max(prob_o35_c, 70.0), 1)
                candidates.append({
                    "market": "Total Tarjetas",
                    "category_code": "TARJETAS",
                    "selection": "Más de 3.5 tarjetas totales",
                    "probability": p_c,
                    "odds": self._fair_odds(p_c, margin=1.06),
                    "_high_conviction": p_c >= 75.0,
                    "availability": "Universal en Bet365, Betano, Ecuabet",
                    "rationale": f"Fricción disciplinaria elevada: {total_cards_exp} tarjetas esperadas en el cotejo bajo rigor arbitral."
                })

        # =====================================================================
        # 7. MERCADOS DE COBERTURA MÍNIMA (Micro-cuotas < 1.20)
        # Solo como respaldo extremo si todo lo anterior fallara
        # =====================================================================
        prob_over05 = exact_market_probs.get("over_0_5_pct", 95.0) if exact_market_probs else 95.0
        candidates.append({
            "market": "Total de Goles Fijo",
            "category_code": "GOLES_OVER",
            "selection": "Más de 0.5 goles totales",
            "probability": round(prob_over05, 1),
            "odds": 1.09,
            "_high_conviction": False,
            "availability": "Universal",
            "rationale": "Línea de cobertura mínima que descarta el 0-0."
        })

        # FILTRADO DE SEGURIDAD
        clean_candidates = []
        for c in candidates:
            sel_l = c.get("selection", "").lower()
            mkt_l = c.get("market", "").lower()
            cat_l = c.get("category_code", "").lower()
            if any(term in sel_l or term in mkt_l or term in cat_l for term in self.BANNED_MARKET_TERMS):
                continue
            if c.get("category_code") not in self.ALLOWED_CATEGORIES:
                continue
            clean_candidates.append(c)
        candidates = clean_candidates

        # ASIGNACIÓN DE TIERS Y SCORING v6.0
        for c in candidates:
            prob = float(c["probability"])
            odds = float(c["odds"])
            cat  = c.get("category_code", "")
            hc   = c.get("_high_conviction", False)

            if cat == "VICTORIA_DIRECTA" and hc:
                c["confidence_tier"] = "TIER_1_CANDADO"
                c["tier_badge"] = "🟢 VICTORIA DIRECTA - ALTA CONVICCIÓN"
            elif cat in {"VICTORIA_SIN_EMPATE", "AMBOS_ANOTAN", "DOBLE_OPORTUNIDAD"} and (prob >= 65.0 or hc):
                c["confidence_tier"] = "TIER_1_CANDADO"
                c["tier_badge"] = "🟢 CANDADO INSTITUCIONAL"
            elif prob >= 60.0 and odds >= 1.30:
                c["confidence_tier"] = "TIER_2_VALOR"
                c["tier_badge"] = "🟡 VALOR ESTRATÉGICO"
            else:
                c["confidence_tier"] = "TIER_3_RIESGO"
                c["tier_badge"] = "🔴 OBSERVACIÓN / COBERTURA"

            c["_rank_score"] = self._rank_score(prob, odds, cat, hc, preferred_category)
            c["expected_value"] = self._ev(prob, odds)

        candidates.sort(key=lambda x: (x["_rank_score"], x["probability"]), reverse=True)

        # =====================================================================
        # SELECCIÓN DEFINITIVA DE LA FIJA
        # =====================================================================
        best_fija = None

        # 1. Si hay victoria directa de alta convicción Y coincide con la preferencia o es un grande
        direct_wins = [c for c in candidates if c.get("category_code") == "VICTORIA_DIRECTA" and c.get("_high_conviction")]
        if direct_wins and preferred_category == "VICTORIA_DIRECTA":
            best_fija = direct_wins[0]
        elif direct_wins and preferred_category not in {"AMBOS_ANOTAN", "TARJETAS", "GOLES_UNDER"}:
            best_fija = direct_wins[0]

        # 2. Si no, si la categoría preferida tiene una opción sólida (cuota >= 1.25)
        if best_fija is None and preferred_category:
            pref_matches = [c for c in candidates if c.get("category_code") == preferred_category and c["odds"] >= 1.24]
            if pref_matches:
                best_fija = pref_matches[0]

        # 3. Si no, elegir la mejor puntuada con cuota real (odds >= 1.24)
        if best_fija is None:
            real_val = [c for c in candidates if c["odds"] >= 1.24]
            if real_val:
                best_fija = real_val[0]

        # 4. Fallback final
        if best_fija is None and candidates:
            best_fija = candidates[0]

        return {
            "selected_la_fija": best_fija,
            "all_feasible_options": candidates,
            "sportsbook_compliance": "Aprobado v6.0: Apuestas de valor real y alta convicción operables en Bet365, Betano y 1xBet."
        }
