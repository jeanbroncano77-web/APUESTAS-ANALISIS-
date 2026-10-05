# -*- coding: utf-8 -*-
"""
AutonomousSportsDaemon:
Daemon autónomo 24/7 de Inteligencia Deportiva con Auto-Retroalimentación Continua.
Opera sin intervención humana:
1. Rastrea actualizaciones de convocatorias, lesiones y alineaciones confirmadas.
2. Actualiza cuotas de mercado y líneas reales.
3. Ejecuta proyecciones con TimesFM y Monte Carlo Dixon-Coles.
4. Liquida partidos finalizados, calcula Brier Score, Win Rate y PnL.
5. Ejecuta el ciclo de auto-retroalimentación (Self-Feedback Loop) para calibrar pesos.
6. Actualiza el Dashboard web y mantiene el servicio activo.
"""

import os
import sys
import time
import json
from datetime import datetime

# Garantizar codificación UTF-8 en consola de Windows
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Rutas del entorno
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.abspath(os.path.join(current_dir, ".."))
if base_dir not in sys.path:
    sys.path.insert(0, base_dir)

from sports_agents import SportsDirectorAgent

FEEDBACK_LOG_PATH = os.path.join(current_dir, "autonomous_feedback_log.json")
AUDIT_RESULTS_PATH = os.path.join(base_dir, "winrate_audit_results.json")
INDEX_PATH = os.path.join(base_dir, "index.html")
ROOT_INDEX_PATH = os.path.abspath(os.path.join(base_dir, "..", "index.html"))


def log_event(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] [AUTONOMOUS DAEMON] {message}"
    try:
        print(entry, flush=True)
    except Exception:
        safe_entry = entry.encode("ascii", errors="replace").decode("ascii")
        print(safe_entry, flush=True)


def init_feedback_log():
    if not os.path.exists(FEEDBACK_LOG_PATH):
        initial_data = {
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "cycles_completed": 0,
            "calibrations": [],
            "current_weights": {
                "squad_offense_penalty": 0.82,
                "minimum_draw_floor": 26.0,
                "corner_game_state_dampener": 0.85,
                "player_sot_restriction_factor": 0.35
            },
            "last_auto_audit": {}
        }
        with open(FEEDBACK_LOG_PATH, "w", encoding="utf-8") as f:
            json.dump(initial_data, f, ensure_ascii=False, indent=2)


def run_autonomous_cycle(cycle_num: int, is_daily_730_run: bool = False):
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if is_daily_730_run:
        log_event(f"⭐⭐ HITO DIARIO 19:30 (7:30 PM) ALCANZADO ⭐⭐")
        log_event("Ejecutando actualización mayor de cartelera 24h anticipada con los 12 agentes...")
    else:
        log_event(f"Iniciando ciclo autónomo de supervisión #{cycle_num}...")

    try:
        from sports_agents.run_daily_cloud import main as run_cloud_pipeline
        run_cloud_pipeline()
        log_event(f"-> Ciclo #{cycle_num} completado exitosamente con 12 agentes, calendario oficial y autoaprendizaje.")
    except Exception as e:
        log_event(f"Error ejecutando ciclo #{cycle_num}: {e}")


def main():
    log_event("=== MOTOR AUTÓNOMO DE INTELIGENCIA DEPORTIVA INICIADO ===")
    log_event("Modo: Supervisión Continua 24/7 sin necesidad de comandos manuales.")
    log_event("Programación Clave: Actualización mayor diaria a las 19:30 (7:30 PM).")
    init_feedback_log()

    cycle = 1
    # Chequeo continuo cada 60 segundos para precisión exacta del reloj a las 19:30
    SCAN_INTERVAL_SECONDS = 60
    # Intervalo de simulación periódica regular: cada 30 minutos
    PERIODIC_CYCLE_MINUTES = 30
    last_periodic_run = time.time()
    last_daily_run_date = ""

    while True:
        try:
            now = datetime.now()
            today_str = now.strftime("%Y-%m-%d")
            current_minute_str = now.strftime("%H:%M")

            # 1. ¿Es la hora fijada (19:30) y no se ha ejecutado hoy?
            if current_minute_str == "19:30" and last_daily_run_date != today_str:
                log_event("Reloj del sistema: 19:30 en punto detectado.")
                run_autonomous_cycle(cycle, is_daily_730_run=True)
                cycle += 1
                last_daily_run_date = today_str
                last_periodic_run = time.time()
            
            # 2. ¿Toca ciclo periódico de 30 minutos?
            elif (time.time() - last_periodic_run) >= (PERIODIC_CYCLE_MINUTES * 60):
                run_autonomous_cycle(cycle, is_daily_730_run=False)
                cycle += 1
                last_periodic_run = time.time()

            time.sleep(SCAN_INTERVAL_SECONDS)
        except Exception as e:
            log_event(f"Error detectado en ciclo #{cycle}: {str(e)}. Reintentando en 60 segundos...")
            time.sleep(60)


if __name__ == "__main__":
    main()
