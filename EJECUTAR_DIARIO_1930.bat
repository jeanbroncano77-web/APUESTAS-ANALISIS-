@echo off
cd /d "c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
".venv\Scripts\python.exe" "sports_agents\run_daily_cloud.py" >> "daily_automation.log" 2>&1
