from cryptography.fernet import Fernet
import os
# 1. Agregamos find_dotenv aquí al final
from dotenv import load_dotenv, find_dotenv 

# 2. Le decimos a dotenv que use su radar para buscar el archivo en las carpetas de arriba
load_dotenv(find_dotenv())

# El resto de tu código se queda intocable:
LLAVE_SECRETA = os.getenv("MI_LLAVE_MAESTRA")

if not LLAVE_SECRETA:
    raise ValueError("¡Falta la llave secreta en el archivo .env!")

cifrador = Fernet(LLAVE_SECRETA)

def encriptar_texto(texto_normal: str) -> str:
    """
    Toma un texto legible, lo convierte a bytes, lo encripta con la llave maestra,
    y devuelve el texto convertido en un código secreto.
    """
    try:
        # Pasamos el texto a bytes
        texto_en_bytes = texto_normal.encode('utf-8')
        
        # Encriptamos usando la llave
        texto_oculto = cifrador.encrypt(texto_en_bytes)
        
        # Devolvemos a String para la página web
        return texto_oculto.decode('utf-8')
    except Exception as e:
        return f"Error al encriptar: {str(e)}" 