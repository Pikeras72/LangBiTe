import os
from huggingface_hub import login

# Intenta autenticarte con tu API Key de HuggingFace
huggingface_api_key = os.getenv('API_KEY_HUGGINGFACE')

if not huggingface_api_key:
    print("¡No se encontró la clave de HuggingFace!")
else:
    try:
        login(huggingface_api_key)
        print("Conexión exitosa con HuggingFace.")
    except Exception as e:
        print(f"Hubo un error al intentar conectar con HuggingFace: {e}")
