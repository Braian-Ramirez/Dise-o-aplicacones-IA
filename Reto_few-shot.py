import os
from google import genai
from dotenv import load_dotenv

# Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GENAI_API_KEY")

# Inicializar el Cliente
client = genai.Client(api_key=API_KEY)

# =====================================================================
# Reto: Few-Shot Prompting
# Clasificador de sentimientos para reseñas de libros
# =====================================================================

resenas_a_evaluar = [
    # 1. Reseña Negativa (La original del reto)
    "Este libro empezó bien pero el final fue muy apresurado y decepcionante.",
    
    # 2. Reseña Positiva (Añadida extra)
    "Una obra maestra absoluta. La narrativa te atrapa desde el primer capítulo y no te suelta hasta la última palabra. Recomendadísimo.",
    
    # 3. Reseña Neutral (Añadida extra)
    "Es un libro informativo y cumple con explicar el tema, aunque la lectura a veces se vuelve un poco monótona y le falta fluidez."
]

PROMPT_BASE = """
Eres un clasificador de sentimientos para reseñas de libros. 
Tu tarea es leer una reseña y responder ÚNICAMENTE con una de las siguientes palabras: POSITIVO, NEUTRAL o NEGATIVO.

Reseña: "Me encantó cada página de esta novela, los personajes están maravillosamente desarrollados y la trama es fascinante."
Sentimiento: POSITIVO

Reseña: "El libro es simplemente uno más del montón, ni muy bueno ni muy malo. Está bien para pasar el rato."
Sentimiento: NEUTRAL

Reseña: "No pude ni terminar de leer la primera mitad. La historia no tiene ningún sentido y los diálogos son absurdos."
Sentimiento: NEGATIVO

Reseña: "{resena}"
Sentimiento:
"""

print("--- Iniciando Generación de Contenido para Reto Few-Shot ---")

# Llamada al servicio de modelos para cada reseña
for i, resena in enumerate(resenas_a_evaluar, 1):
    prompt_completo = PROMPT_BASE.format(resena=resena)
    print(f"\n--- Evaluando Reseña {i} ---")
    print(f'"{resena}"')
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt_completo,
        )
        
        # Imprimir la respuesta
        print("\n✅ Respuesta del modelo (Clasificación):")
        print(response.text.strip())

    except Exception as e:
        print(f"\n❌ Ocurrió un error al procesar el prompt: {e}")
