from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil
import os
from backend.transcriber import transcribir_audio 
# AQUÍ ESTÁ EL IMPORT QUE FALTABA
from backend.crypto_utils import encriptar_texto 

app = FastAPI(title="API de Transcripción de Audio IA")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ruta_raiz():
    return {"estado": "Online", "mensaje": "¡El servidor Backend de IA está funcionando!"}

@app.post("/procesar-audio")
async def procesar_audio(audio: UploadFile = File(...)):
    # 1. Definimos dónde guardar temporalmente
    ruta_temporal = f"temp_audios/{audio.filename}"
    
    # 2. Guardamos el MP3
    with open(ruta_temporal, "wb") as buffer:
        shutil.copyfileobj(audio.file, buffer)
        
    # 3. La IA saca el texto original (Una sola vez)
    texto_extraido = transcribir_audio(ruta_temporal)
    
    # 4. Encriptamos el texto extraído
    texto_seguro = encriptar_texto(texto_extraido)
    
    # 5. Borramos el audio para limpiar
    os.remove(ruta_temporal)
    
    # 6. Devolvemos el resultado final
    return {
        "archivo": audio.filename,
        "texto_original": texto_extraido,
        "texto_encriptado": texto_seguro
    }