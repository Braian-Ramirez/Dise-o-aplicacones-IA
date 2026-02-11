# Guía de Ejecución del Proyecto Gemini API

Este proyecto implementa una conexión básica con la API de Google Gemini utilizando Python. A continuación se detallan los pasos para configurar y ejecutar el código correctamente.

## Estructura del Proyecto

*   **`gemini_api.py`**: Script principal que conecta con la API de Gemini y realiza una consulta de prueba.
*   **`prueba_entorno.py`**: Script de utilidad para verificar que el entorno virtual está activo y que existe conexión a internet.
*   **`requirements.txt`**: Archivo que lista todas las librerías necesarias para el proyecto.
*   **`.env`**: Archivo de configuración donde se debe almacenar la clave de API (API Key).

---

## Instrucciones Paso a Paso

### 1. Prerrequisitos

Asegúrate de tener **Python** instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/).

### 2. Configuración del Entorno Virtual

Es una buena práctica utilizar un entorno virtual para no instalar dependencias en todo el sistema.

**En Windows:**

1.  Abre tu terminal (PowerShell o CMD) en la carpeta del proyecto.
2.  Crea el entorno virtual:
    ```bash
    python -m venv env
    ```
3.  Activa el entorno virtual:
    ```bash
    .\env\Scripts\activate
    ```

**En macOS/Linux:**

1.  Abre tu terminal en la carpeta del proyecto.
2.  Crea el entorno virtual:
    ```bash
    python3 -m venv env
    ```
3.  Activa el entorno virtual:
    ```bash
    source env/bin/activate
    ```

> Verás que el prompt de tu terminal cambia indicando `(env)`, lo cual confirma que el entorno está activo.

### 3. Instalación de Dependencias

Con el entorno virtual activado, instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

### 4. Configuración de la API Key

Para que el script pueda comunicarse con Google Gemini, necesitas configurar tu clave de seguridad.

1.  Crea un archivo nuevo llamado `.env` en la misma carpeta donde están los scripts (si no existe ya).
2.  Abre el archivo `.env` con un editor de texto (como Notepad o VS Code).
3.  Agrega la siguiente línea, reemplazando `TU_CLAVE_AQUI` por tu clave real de Gemini:

```ini
GEMINI_API_KEY=TU_CLAVE_AQUI
```

### 5. Verificación del Entorno (Opcional)

Antes de correr el programa principal, puedes verificar que todo esté en orden ejecutando el script de prueba:

```bash
python prueba_entorno.py
```

Si todo es correcto, verás mensajes confirmando que el entorno virtual está activo y que hay conexión a internet.

### 6. Ejecución del Código

Finalmente, para probar la conexión con Gemini y recibir una respuesta, ejecuta:

```bash
python gemini_api.py
```

Si la configuración es exitosa, verás en la consola la respuesta generada por el modelo de IA.
