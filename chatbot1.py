import nltk
from nltk.chat.util import Chat, reflections

# Configuración de reglas y respuestas del chatbot
pares = [
    [
        r"¿Cómo está el clima hoy\??",
        ["El clima actual es soleado y cálido.", "Hoy hace un día hermoso."],
    ],
    [
        r"¿Cuál es el pronóstico del clima para mañana\??",
        ["Mañana se espera un clima soleado con temperaturas altas.", "Mañana será un día agradable."],
    ],
    [
        r"¿Hace frío\??",
        ["No, el clima es cálido en este momento.", "No, no hace frío en absoluto."],
    ],
    [
        r"Adiós",
        ["Adiós, ¡que tengas un buen día!", "Hasta luego."],
    ],
    [
        r"Que hora es\??",
        ["Lo siento no comprendo la peticion"],
    ]   
]

# Crear un chatbot con las reglas definidas
chatbot = Chat(pares, reflections)

# Iniciar el chatbot
print("Hola, Mi nombre es Max. Puedes preguntarme sobre el clima actual¿Cómo está el clima hoy? y el pronóstico del tiempo.")
chatbot.converse()