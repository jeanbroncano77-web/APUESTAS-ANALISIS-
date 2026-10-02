' Script VBS para ejecutar el daemon de SportsAI de manera 100% invisible y silenciosa
' No abre ventanas de consola ni interrumpe al usuario.
Set WshShell = CreateObject("WScript.Shell")
strPath = "c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"
strPython = strPath & "\.venv\Scripts\python.exe"
strScript = strPath & "\sports_agents\autonomous_sports_daemon.py"
strCommand = """" & strPython & """ """ & strScript & """"
WshShell.CurrentDirectory = strPath
WshShell.Run strCommand, 0, False
Set WshShell = Nothing
