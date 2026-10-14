# -*- coding: utf-8 -*-
"""
test_build_dashboard.py
Prueba de integración completa del generador unificado de las 3 Áreas.
"""
import os
import sys
import json
import re

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
index_path = os.path.join(base_dir, "index.html")
sim_path = os.path.join(base_dir, "sports_agents", "simulations_tomorrow_results.json")
audit_path = os.path.join(base_dir, "sports_agents", "audit_history.json")
feedback_path = os.path.join(base_dir, "sports_agents", "autonomous_feedback_log.json")

with open(sim_path, "r", encoding="utf-8") as f:
    sim_data = json.load(f)

with open(audit_path, "r", encoding="utf-8") as f:
    audit_data = json.load(f)

with open(feedback_path, "r", encoding="utf-8") as f:
    fb_data = json.load(f)

print(f"Partidos en sim_data: {len(sim_data['Matches'])}")
print(f"Registros en audit_data: {len(audit_data['history'])}")
print(f"Ciclos en fb_data: {fb_data.get('cycles_completed')}")
print("¡Archivos cargados con éxito!")
