@echo off
chcp 65001 > nul
echo ========================================================
echo   REGISTRAR SPORTSAI COMO TAREA AUTÓNOMA DE WINDOWS
echo ========================================================
echo.
echo Este script registra SportsAI en el Programador de Tareas
echo de Windows para que funcione SIEMPRE solo en segundo plano,
echo sin necesidad de abrir Antigravity IDE ni ninguna consola.
echo.

set TASKNAME="SportsAI_Autonomous_Daemon"
set VBSPATH="c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo\EJECUTAR_SILENCIOSO.vbs"

echo Registrando tarea '%TASKNAME%' para iniciar en cada inicio de sesión...
schtasks /create /tn %TASKNAME% /tr "wscript.exe \"%VBSPATH%\"" /sc onlogon /rl highest /f

if %errorlevel% equ 0 (
    echo.
    echo ========================================================
    echo  [EXITO] Tarea autónoma registrada correctamente en Windows!
    echo ========================================================
    echo El motor se iniciará automáticamente cada vez que inicies tu PC.
    echo.
    echo Iniciando tarea ahora mismo en segundo plano...
    schtasks /run /tn %TASKNAME%
) else (
    echo.
    echo [!] Si el comando falló, ejecuta este archivo como Administrador.
)

echo.
pause
