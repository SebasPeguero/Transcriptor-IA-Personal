@echo off
title Servidor de Transcripcion IA By Sebas
color 0A

echo ===================================================
echo   INICIANDO EL CEREBRO DE INTELIGENCIA ARTIFICIAL
echo ===================================================
echo.

:: 1. Viajar a la carpeta de tu proyecto
cd /d "D:\itla semestre 4\Desarrollo de IA\PoyectoMP3ATxt"

:: 2. Activar el entorno virtual
call venv\Scripts\activate

:: 3. Abrir la pagina web automaticamente en tu navegador
start frontend\index.html

:: 4. Encender el servidor Backend
echo Encendiendo el motor de FastAPI y Whisper...
uvicorn backend.main:app

pause