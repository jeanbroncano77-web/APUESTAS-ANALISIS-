import os
import sys
import json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sys.path.insert(0, base_dir)

from sports_agents.feedback_engine import FeedbackEngine

engine = FeedbackEngine()
brier = engine.compute_brier_score()
cats = engine.compute_category_performance()
entry = engine.generate_cycle_entry(
    cycle_num=108,
    target_day="Lunes",
    target_date="19/10/2026",
    fija_conf_avg=64.5
)
engine.record_cycle(entry)

print("FeedbackEngine 3.0 actualizado para Ciclo #108:")
print(f"  Brier Score: {brier}")
print(f"  Salud: {entry['system_health']}")
print(f"  Observaciones: {len(entry['observations'])}")
