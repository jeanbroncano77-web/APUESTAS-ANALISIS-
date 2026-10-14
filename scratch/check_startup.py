import subprocess
import os

print("--- 1. Startup Folder ---")
startup_user = os.path.expandvars(r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
if os.path.exists(startup_user):
    for f in os.listdir(startup_user):
        print(f"User Startup: {f}")

startup_common = os.path.expandvars(r"%PROGRAMDATA%\Microsoft\Windows\Start Menu\Programs\Startup")
if os.path.exists(startup_common):
    for f in os.listdir(startup_common):
        print(f"Common Startup: {f}")

print("\n--- 2. Scheduled Tasks ---")
res = subprocess.run(["schtasks", "/query", "/fo", "LIST", "/v"], capture_output=True, text=True, errors="replace")
for block in res.stdout.split("\n\n"):
    lower = block.lower()
    if any(k in lower for k in ["analisis", "sport", "daily", "cloud", "730", "daemon", "antigravity"]):
        print("Found Task:")
        for line in block.splitlines():
            if any(k in line.lower() for k in ["taskname", "task name", "task to run", "nombre de tarea", "tarea que se ejecutar", "desencadenador", "author", "autor"]):
                print("  ", line.strip())

print("\n--- 3. Registry Run keys ---")
res_reg = subprocess.run(["reg", "query", r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run"], capture_output=True, text=True, errors="replace")
print("HKCU Run:\n", res_reg.stdout)

res_reg_lm = subprocess.run(["reg", "query", r"HKLM\Software\Microsoft\Windows\CurrentVersion\Run"], capture_output=True, text=True, errors="replace")
print("HKLM Run:\n", res_reg_lm.stdout)
