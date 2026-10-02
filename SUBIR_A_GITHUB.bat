@echo off
chcp 65001 > nul
echo ========================================================
echo    SUBIENDO SPORTSAI DASHBOARD A TU REPOSITORIO GITHUB
echo ========================================================
echo.
cd /d "c:\Users\jeanb\Documents\Antigravity Proyectos\Analisis deportivo"

echo 1. Verificando estado local...
git status -s

echo.
echo 2. Subiendo a: https://github.com/jeanbroncano77-web/APUESTAS-ANALISIS-.git
echo (Si se abre una ventana del navegador, autoriza el inicio de sesion)
echo.
git push -u origin main

echo.
if %errorlevel% equ 0 (
    echo ========================================================
    echo  SUBIDA EXITOSA A GITHUB!
    echo ========================================================
    echo.
    echo Tu repositorio esta listo en:
    echo https://github.com/jeanbroncano77-web/APUESTAS-ANALISIS-
    echo.
    echo Ahora solo activa GitHub Pages:
    echo 1. Ve a: https://github.com/jeanbroncano77-web/APUESTAS-ANALISIS-/settings/pages
    echo 2. En 'Branch' selecciona 'main' y guarda.
    echo.
    echo Tu enlace 24/7 permanente sera:
    echo https://jeanbroncano77-web.github.io/APUESTAS-ANALISIS-/
    echo ========================================================
) else (
    echo.
    echo [!] Hubo un error de autenticacion. Asegurate de autorizar en GitHub.
)
echo.
pause
