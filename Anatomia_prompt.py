import os
from google import genai
from dotenv import load_dotenv

# Cargar configuración de variables de entorno
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GENAI_API_KEY")

# Inicializar el Cliente
client = genai.Client(api_key=API_KEY)

# =====================================================================
# Parte 1: La Anatomía del Prompt (Estructura)
# Transformando un "Prompt Débil" en un "Prompt Maestro"
# =====================================================================

# Prompt Débil original: "Escribe un correo para un cliente que no ha pagado."

PROMPT_MAESTRO = """
Eres un Gerente de Finanzas amable pero firme. (Persona / Tono)

Tu tarea es escribir un correo electrónico profesional dirigido a un cliente que tiene facturas vencidas y no ha pagado. (Tarea)

El objetivo es recordarles amablemente sobre su deuda y solicitar el pago lo antes posible para no afectar la relación comercial, manteniendo siempre una postura comprensiva pero firme respecto a nuestras políticas de cobro. (Contexto)

A continuación te proporciono los datos del cliente y los montos.
Usa los delimitadores ### para separar los datos del cliente del resto de la instrucción. (Delimitadores)

###
Nombre del Cliente: Empresa XYZ
Facturas vencidas: F-1234, F-1235
Días de retraso: 45 días
Monto Total Adeudado: $5,400.00 USD
###

Asegúrate de que el correo tenga una estructura clara y un saludo profesional.
Además, el correo DEBE terminar obligatoriamente con un resumen en una tabla de los montos adeudados, mostrando número de factura y monto. (Formato)
"""

print("--- Iniciando Generación de Contenido para Anatomía del Prompt ---")
print("Prompt Maestro seleccionado:\n", PROMPT_MAESTRO)
print("-----------------------------------------")

# Llamada al servicio de modelos
try:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=PROMPT_MAESTRO,
    )
    
    # Imprimir la respuesta
    print("\n✅ Respuesta del modelo:\n")
    print(response.text)

except Exception as e:
    print(f"\n❌ Ocurrió un error al procesar el prompt: {e}")
