import os
from google import genai
from dotenv import load_dotenv

# 1. Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GENAI_API_KEY")

# 2. Inicializar el Cliente
client = genai.Client(api_key=API_KEY)

# =====================================================================
# SECCIÓN DE PROMPTS QUEMADOS (HARDCODED)
# Aquí puedes detallar tus prompts dejándolos fijos en el código
# =====================================================================

PROMPT_1 = """
Escribe una publicación de blog detallada sobre las ventajas de us
ar microservicios.
"""

PROMPT_2 = """
Genera una lista de 3 lenguajes de programación. FORMATO: Devuelve
el resultado exclusivamente en formato JSON con las llaves 'nombre' y 'uso_pri
ncipal'.
"""

PROMPT_3 = """
Explica el concepto de 'Entropía' aplicado a la teoría de la infor
mación.
"""
PROMPT_4 = """
Explica qué es una base de datos.TONO: Escribe como si fueras un p
irata del siglo XVIII utilizando jerga náutica.
"""
PROMPT_5 = """
Explica cómo funciona el protocolo HTTP. CONTEXTO: Tu audiencia so
n niños de 8 años en una clase de introducción a la tecnología.
"""
PROMPT_6 = """
Resume el impacto de la revolución industrial. RESTRICCIONES: No u
ses más de 50 palabras. No menciones a ningún personaje histórico específic
o.
"""
PROMPT_7 = """
Explica qué es una base de datos.TONO: Escribe como si fueras un p
irata del siglo XVIII utilizando jerga náutica.
"""

# Selecciona cuál prompt quieres ejecutar cambiando esta variable
prompt_a_ejecutar = PROMPT_4

print("--- Iniciando Generación de Contenido ---")
print("Prompt seleccionado:\n", prompt_a_ejecutar)
print("-----------------------------------------")

# 3. Llamada al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt_a_ejecutar,
    )
    
    # 4. Imprimir la respuesta
    print("\n✅ Respuesta del modelo:\n")
    print(response.text)

except Exception as e:
    print(f"\n❌ Ocurrió un error al procesar el prompt: {e}")
