import subprocess

vbs_path = r'c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo\EJECUTAR_DIARIO_1930.vbs'
cmd = ['schtasks', '/create', '/tn', 'SportsAI_Daily_1930', '/tr', f'wscript.exe "{vbs_path}"', '/sc', 'daily', '/st', '19:30', '/f']

print("Running:", ' '.join(cmd))
res = subprocess.run(cmd, capture_output=True, text=True)
print("Return code:", res.returncode)
print("Stdout:", res.stdout)
print("Stderr:", res.stderr)
