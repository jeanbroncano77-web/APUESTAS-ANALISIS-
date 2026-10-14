import subprocess
import csv
import io

res = subprocess.run(["schtasks", "/query", "/v", "/fo", "CSV"], capture_output=True, text=True, errors="replace")
reader = csv.DictReader(io.StringIO(res.stdout))
for row in reader:
    name = row.get("Nombre de tarea") or row.get("TaskName") or ""
    run = row.get("Tarea que se ejecutará") or row.get("Task To Run") or ""
    lower = (name + " " + run).lower()
    if any(k in lower for k in ["sports", "jeanb", "antigravity", "analisis"]):
        print(f"Task: {name}\n  Run: {run}\n  Type: {row.get('Tipo de programación')}\n  Next: {row.get('Hora próxima ejecución')}\n")
