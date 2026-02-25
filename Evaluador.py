import os
from google import genai
from dotenv import load_dotenv

# Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GENAI_API_KEY")

# Inicializar el Cliente
client = genai.Client(api_key=API_KEY)

# =====================================================================
# Parte 4: El Evaluador
# Evaluador académico de ensayos con condicionales y salida JSON
# =====================================================================

ensayos_a_evaluar = [
    # 1. Ensayo corto (< 100 palabras)
    "La inteligencia artificial es muy buena. Me gusta cómo puede generar texto e imágenes rápidamente. Creo que en el futuro todos usaremos IA para trabajar y estudiar, ya que nos facilita mucho la vida.",
    
    # 2. Ensayo largo (> 100 palabras)
    "El impacto de la inteligencia artificial en la sociedad moderna es innegable. Por un lado, la automatización impulsada por estas tecnologías promete aumentar significativamente la eficiencia productiva, lo que podría traducirse en un crecimiento económico sin precedentes. Sin embargo, no se pueden ignorar los desafíos éticos y laborales que esto conlleva. La posible pérdida de empleos en sectores tradicionales requiere de políticas públicas enfocadas en la reconversión laboral y la educación continua. Además, está la cuestión de los sesgos algorítmicos, que pueden perpetuar discriminaciones existentes si no se abordan adecuadamente desde las fases de diseño de los sistemas. En conclusión, si bien la inteligencia artificial representa una herramienta con un potencial transformador enorme, su implementación debe ser guiada por un debate ético riguroso y una planificación social cuidadosa para asegurar que sus beneficios se distribuyan equitativamente en toda la sociedad."
]

PROMPT_EVALUADOR = """
Rol: Eres un evaluador académico de ensayos estricto y profesional.

Instrucciones:
Se te proporcionará un ensayo delimitado por tres comillas dobles (\"\"\").
Debes analizar el texto y seguir estas reglas al pie de la letra:

1. Condicional de longitud:
   - Cuenta el número aproximado de palabras del ensayo.
   - SI el ensayo tiene MENOS de 100 palabras: Debes rechazarlo y pedir más contenido.
   - SI el ensayo tiene 100 palabras o MÁS: Debes evaluarlo bajo los siguientes criterios:
     * Ortografía
     * Coherencia
     * Argumentación

2. Formato de Salida:
   - Tu respuesta DEBE ser ÚNICAMENTE un objeto JSON válido, sin texto adicional antes ni después.
   - El JSON debe contener exactamente dos llaves: "nota_final" (un número del 0 al 10 o un mensaje de rechazo) y "comentarios" (una cadena de texto con el detalle de la evaluación o el motivo del rechazo).

Ejemplo de salida JSON para ensayo rechazado:
{{
  "nota_final": "N/A",
  "comentarios": "Ensayo rechazado. El texto tiene menos de 100 palabras. Por favor, desarrolle más sus ideas y envíe un ensayo más completo."
}}

Ejemplo de salida JSON para ensayo evaluado:
{{
  "nota_final": 8.5,
  "comentarios": "Ortografía: Excelente. Coherencia: Buena, aunque en el segundo párrafo las ideas saltan abruptamente. Argumentación: Sólida, presenta buenos puntos pero faltan ejemplos."
}}

Ensayo a evaluar:
\"\"\"{ensayo}\"\"\"
"""

print("--- Iniciando Generación de Contenido: El Evaluador ---")

# Llamada al servicio de modelos para cada ensayo
for i, ensayo in enumerate(ensayos_a_evaluar, 1):
    prompt_completo = PROMPT_EVALUADOR.format(ensayo=ensayo)
    print(f"\n--- Evaluando Ensayo {i} ---")
    print(f'"{ensayo[:50]}..." (Aprox. {len(ensayo.split())} palabras)')
    
    try:
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt_completo,
            config={
                "response_mime_type": "application/json",
            }
        )
        
        # Imprimir la respuesta
        print("\n✅ Respuesta del modelo (JSON):")
        print(response.text.strip())

    except Exception as e:
        print(f"\n❌ Ocurrió un error al procesar el prompt: {e}")
