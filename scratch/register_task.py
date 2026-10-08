import subprocess

vbs_path = r'c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo\EJECUTAR_DIARIO_1930.vbs'
cmd1 = ['schtasks', '/create', '/tn', 'SportsAI_Daily_1930', '/tr', f'wscript.exe "{vbs_path}"', '/sc', 'daily', '/st', '19:30', '/f']
res1 = subprocess.run(cmd1, capture_output=True, text=True)
print("19:30 task:", res1.stdout)

cmd2 = ['schtasks', '/create', '/tn', 'SportsAI_Daily_0730', '/tr', f'wscript.exe "{vbs_path}"', '/sc', 'daily', '/st', '07:30', '/f']
res2 = subprocess.run(cmd2, capture_output=True, text=True)
print("07:30 task:", res2.stdout)
