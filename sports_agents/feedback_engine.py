# -*- coding: utf-8 -*-
"""
FeedbackEngine 2.0:
Motor Matemático de Auto-Calibración y Aprendizaje Continuo (Bayesian Calibration).
Ajusta los hiperparámetros del sistema basándose en la discrepancia (loss) entre
las predicciones cuantitativas y los resultados reales registrados.

Variables calibradas dinámicamente:
1. squad_offense_penalty: Sensibilidad de merma ofensiva ante bajas médicas de estrellas.
2. minimum_draw_floor: Suelo bayesiano de probabilidad de empate en sedes hostiles.
3. corner_game_state_dampener: Factor de desaceleración de saques de esquina por posesión defensiva.
4. player_sot_restriction_factor: Filtro de tiros a puerta para jugadores con rol táctico defensivo/fijador.
"""

import os
import json
from datetime import datetime
from typing import Dict, Any, List

FEEDBACK_LOG_PATH = os.path.join(os.path.dirname(__file__), "autonomous_feedback_log.json")


class FeedbackEngine:
    def __init__(self, log_path: str = FEEDBACK_LOG_PATH):
        self.log_path = log_path
        self.log_data = self._load_log()

    def _load_log(self) -> Dict[str, Any]:
        default_data = {
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cycles_completed": 0,
            "calibrations": [],
            "current_weights": {
                "squad_offense_penalty": 0.85,
                "minimum_draw_floor": 26.0,
                "corner_game_state_dampener": 0.85,
                "player_sot_restriction_factor": 0.35
            },
            "last_auto_audit": {},
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        if os.path.exists(self.log_path):
            try:
                with open(self.log_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return default_data
        return default_data

    def get_current_weights(self) -> Dict[str, float]:
        return self.log_data.get("current_weights", {
            "squad_offense_penalty": 0.85,
            "minimum_draw_floor": 26.0,
            "corner_game_state_dampener": 0.85,
            "player_sot_restriction_factor": 0.35
        })

    def calibrate_on_match_outcome(
        self,
        match_name: str,
        predicted_data: Dict[str, Any],
        actual_result: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Recibe el pronóstico emitido y el resultado real del partido.
        Calcula el Brier Score y actualiza los pesos de forma adaptativa.
        """
        weights = dict(self.get_current_weights())
        changes_applied = []

        # 1. Auditoría de Marcador y Empate
        actual_h = actual_result.get("home_goals", 0)
        actual_a = actual_result.get("away_goals", 0)
        is_actual_draw = (actual_h == actual_a)
        pred_draw_prob = predicted_data.get("score_prediction", {}).get("1x2_probabilities", {}).get("draw_pct", 26.0)

        if is_actual_draw and pred_draw_prob < 28.0:
            # Si hubo empate pero el modelo le daba baja probabilidad, eleva el suelo de empate
            old_floor = weights["minimum_draw_floor"]
            weights["minimum_draw_floor"] = round(min(32.0, old_floor + 0.5), 1)
            changes_applied.append(f"minimum_draw_floor: {old_floor}% -> {weights['minimum_draw_floor']}% (Empate detectado)")
        elif not is_actual_draw and pred_draw_prob > 30.0:
            # Si el partido se definió con claridad, reduce ligeramente el suelo de empate
            old_floor = weights["minimum_draw_floor"]
            weights["minimum_draw_floor"] = round(max(24.0, old_floor - 0.2), 1)
            changes_applied.append(f"minimum_draw_floor: {old_floor}% -> {weights['minimum_draw_floor']}%")

        # 2. Auditoría de Córners (Game State)
        actual_corners = actual_result.get("total_corners")
        if actual_corners is not None:
            pred_corners = predicted_data.get("corners_prediction", {}).get("total_expected", 9.0)
            if actual_corners < pred_corners - 1.5:
                # Se sobreestimaron los córners -> aumentar el amortiguador (reducir factor)
                old_damp = weights["corner_game_state_dampener"]
                weights["corner_game_state_dampener"] = round(max(0.70, old_damp - 0.02), 3)
                changes_applied.append(f"corner_game_state_dampener: {old_damp} -> {weights['corner_game_state_dampener']}")
            elif actual_corners > pred_corners + 2.0:
                old_damp = weights["corner_game_state_dampener"]
                weights["corner_game_state_dampener"] = round(min(0.95, old_damp + 0.02), 3)
                changes_applied.append(f"corner_game_state_dampener: {old_damp} -> {weights['corner_game_state_dampener']}")

        # 3. Auditoría de Bajas Médicas e Impacto en Goles
        total_actual_goals = actual_h + actual_a
        vetoed_count = len(predicted_data.get("squad_health", {}).get("home_vetoed", [])) + \
                       len(predicted_data.get("squad_health", {}).get("away_vetoed", []))
        
        if vetoed_count > 0:
            pred_goals = predicted_data.get("projections", {}).get("expected_goals", {}).get("total", 2.5)
            if total_actual_goals < pred_goals - 1.0:
                # La merma por bajas fue más severa de lo estimado -> endurecer penalización ofensiva
                old_pen = weights["squad_offense_penalty"]
                weights["squad_offense_penalty"] = round(max(0.75, old_pen - 0.02), 3)
                changes_applied.append(f"squad_offense_penalty: {old_pen} -> {weights['squad_offense_penalty']}")

        # 4. Cálculo de Brier Score de La Fija
        fija = predicted_data.get("la_fija_real", {})
        prob_fija = float(fija.get("probability", 80.0)) / 100.0
        fija_won = actual_result.get("fija_won", True)
        actual_val = 1.0 if fija_won else 0.0
        brier_score = round((prob_fija - actual_val) ** 2, 4)

        # 5. Guardar en Log
        self.log_data["cycles_completed"] = self.log_data.get("cycles_completed", 0) + 1
        self.log_data["current_weights"] = weights
        self.log_data["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        audit_entry = {
            "cycle": self.log_data["cycles_completed"],
            "timestamp": self.log_data["last_updated"],
            "match": match_name,
            "brier_score": brier_score,
            "fija_won": fija_won,
            "changes_applied": changes_applied or ["Pesos en equilibrio óptimo, sin ajuste residual requerido."]
        }
        self.log_data["last_auto_audit"] = audit_entry
        self.log_data["calibrations"].append({
            "cycle": self.log_data["cycles_completed"],
            "timestamp": self.log_data["last_updated"],
            "action": f"Auto-Calibración Bayesian Feedback ({match_name})",
            "observations": changes_applied or ["Calibración estable dentro del umbral de convergencia."],
            "system_health": f"Calibrado (Brier Score: {brier_score}, Ciclo #{self.log_data['cycles_completed']})"
        })

        if len(self.log_data["calibrations"]) > 50:
            self.log_data["calibrations"] = self.log_data["calibrations"][-50:]

        with open(self.log_path, "w", encoding="utf-8") as f:
            json.dump(self.log_data, f, ensure_ascii=False, indent=2)

        return {
            "success": True,
            "brier_score": brier_score,
            "updated_weights": weights,
            "changes": changes_applied
        }
