# -*- coding: utf-8 -*-
import os

appdata = os.environ.get("APPDATA", "")
if not appdata:
    appdata = os.path.expanduser("~\\AppData\\Roaming")

startup_dir = os.path.join(appdata, "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
os.makedirs(startup_dir, exist_ok=True)
target_vbs = os.path.join(startup_dir, "SportsAI_AutoStart.vbs")

base_dir = r"c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
python_exe = os.path.join(base_dir, ".venv", "Scripts", "python.exe")
daemon_py = os.path.join(base_dir, "sports_agents", "autonomous_sports_daemon.py")

vbs_code = f'''Set WshShell = CreateObject("WScript.Shell")
strPath = "{base_dir}"
strPython = "{python_exe}"
strScript = "{daemon_py}"
strCommand = """" & strPython & """ """ & strScript & """"
WshShell.CurrentDirectory = strPath
WshShell.Run strCommand, 0, False
Set WshShell = Nothing
'''

with open(target_vbs, "w", encoding="utf-8") as f:
    f.write(vbs_code)

print(f"[OK] Archivo de inicio automático creado con éxito en:\n{target_vbs}")
