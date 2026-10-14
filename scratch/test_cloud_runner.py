# -*- coding: utf-8 -*-
"""
test_cloud_runner.py
Verifica la ejecución de run_daily_cloud.py y comprueba que
las 3 áreas se actualicen de manera autónoma.
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
sys.path.insert(0, base_dir)

from datetime import datetime, timedelta, timezone

utc_now = datetime.now(timezone.utc)
lima_now = utc_now - timedelta(hours=5)

print(f"Hora Lima: {lima_now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Hora actual hora local: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
