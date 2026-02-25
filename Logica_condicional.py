import os
from google import genai
from dotenv import load_dotenv

# Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GENAI_API_KEY")

# Inicializar el Cliente
client = genai.Client(api_key=API_KEY)

# =====================================================================
# Lógica Condicional en Prompts
# Asistente de triaje de correos de soporte
# =====================================================================

textos_usuario = [
    # 1. Queja sobre pago o factura
    "Hola, mi factura #4502 tiene un cargo doble que no reconozco. Ayuda.",
    
    # 2. Duda técnica general
    "Buenos días, no puedo conectar mi computadora a la red Wi-Fi de la oficina. Dice que la contraseña es incorrecta.",
    
    # 3. Categoría no identificada
    "Me encantó el artículo que publicaron en su blog sobre la historia de la inteligencia artificial. Muy interesante."
]

PROMPT_BASE = """
Contexto: Eres un asistente de triaje de correos electrónicos de soporte.

Instrucciones: Se te proporcionará un texto delimitado por \"\"\".

1. SI el texto contiene una queja sobre un pago o factura:
    - Clasifícalo como "URGENTE-FINANZAS".
    - Extrae el número de factura si existe.
2. SI NO, si el texto es una duda técnica general:
    - Clasifícalo como "SOPORTE-ESTÁNDAR".
    - Responde: "Gracias, un técnico lo revisará".
3. SI NO es ninguna de las anteriores:
    - Responde simplemente: "Categoría no identificada".

Texto del Usuario: \"\"\"{texto}\"\"\"
"""

print("--- Iniciando Generación de Contenido para Lógica Condicional ---")

# Llamada al servicio de modelos para cada texto
for i, texto in enumerate(textos_usuario, 1):
    prompt_completo = PROMPT_BASE.format(texto=texto)
    print(f"\n--- Evaluando Texto {i} ---")
    print(f'"{texto}"')
    
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt_completo,
        )
        
        # Imprimir la respuesta
        print("\n✅ Respuesta del modelo:")
        print(response.text.strip())

    except Exception as e:
        print(f"\n❌ Ocurrió un error al procesar el prompt: {e}")
