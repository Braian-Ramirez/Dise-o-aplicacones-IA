import os
from google import genai
from dotenv import load_dotenv
 
# 1. Cargar configuración de variables de entorno
load_dotenv()
clave_api = os.getenv("GEMINI_API_KEY")
 
# 2. Inicializar el Cliente
# Este cliente gestiona la conexión
client = genai.Client(api_key=clave_api)
 
def ejecutar_consulta():
    print("🚀 Conectando con el motor de Gemini ...🚈")
    try:
        # 3. Llamada directa al servicio de modelos
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Preséntate como un asistente en el desarrollo y guia de entrenamientos de alto nivel para basketball'"
        )
        print("\n--- Respuesta Recibida ---")
        print(response.text)
        print("--------------------------")
    except Exception as e:
        print(f"❌ Ocurrió un error en la conexión: {e}")
 
if __name__ == "__main__":
    ejecutar_consulta()