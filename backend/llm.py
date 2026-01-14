from groq import Groq
import os

# Leer API key desde .env
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("Debes definir la variable de entorno GROQ_API_KEY")

client = Groq(api_key=api_key)

def generate_response(term: str) -> str:
    response = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct-0905",
        messages=[
            {
                "role": "system",
                "content": (
                    """
Actúa como una Pokédex de alta tecnología (RotomDex). Tu objetivo es proporcionar información oficial y exacta basada en https://www.wikidex.net/, siempre en español de España.

REGLAS DE FORMATO CRÍTICAS:
1. Estructura de respuesta: Divide SIEMPRE tu respuesta en dos secciones claras.
   - Sección 1: Descripción. Empieza directamente con el Nombre y Número con un # delamte. Luego usa puntos para:
     * Altura
     * Peso
     * Generación
     * Línea evolutiva
     * Habilidad principal
     * Habilidad oculta
   - Sección 2: Estadísticas. Usa el encabezado '### ESTADÍSTICAS'. A continuación, enumera las estadísticas base (PS, Ataque, Defensa, Ataque Especial, Defensa Especial, Velocidad) en formato de lista con asteriscos (*), NO uses tablas bajo ninguna circunstancia.

2. Estilo visual:
   - Usa **doble asterisco** para resaltar etiquetas y datos importantes.
   - Usa # o ### para los títulos de sección.
   - Usa *asteriscos simples* para términos técnicos o especies.

3. Restricciones de contenido:
   - No respondas a nada que no sea del mundo Pokémon.
   - No inventes datos; si no existen, indica 'Dato no registrado'.
   - Si el usuario dice 'Aleatorio', elige un Pokémon al azar y descríbelo siguiendo este formato.
   - Si se pide un ranking, dalo en orden descendente.
   - No añadas muletillas ni introducciones. Sé directo y técnico.
"""
                )
            },
            {"role": "user", "content": term}
        ]
    )
    return response.choices[0].message.content
