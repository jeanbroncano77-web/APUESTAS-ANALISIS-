' Script VBS para ejecucion diaria silenciosa a las 19:30
Set WshShell = CreateObject("WScript.Shell")
strPath = "c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
strPython = strPath & "\.venv\Scripts\python.exe"
strScript = strPath & "\sports_agents\run_daily_cloud.py"
strCommand = """" & strPython & """ """ & strScript & """"
WshShell.CurrentDirectory = strPath
WshShell.Run strCommand, 0, True
Set WshShell = Nothing
