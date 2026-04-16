import whisper
import os

# Cargamos el modelo de IA. Usamos el modelo "base" porque es rápido y consume poca RAM.
# (La primera vez que ejecutes esto, descargará unos 74MB de internet)
print("Cargando modelo de IA Whisper...")
modelo = whisper.load_model("base")
print("¡Modelo cargado y listo!")

def transcribir_audio(ruta_archivo: str) -> str:
    """
    Toma la ruta de un archivo de audio (MP3, WAV), se lo pasa a la IA 
    y devuelve el texto transcrito.
    """
    try:
        # Aquí ocurre la magia de la Inteligencia Artificial
        resultado = modelo.transcribe(ruta_archivo)
        return resultado["text"]
    except Exception as e:
        return f"Error al procesar el audio: {str(e)}"