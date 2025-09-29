respuestas = {
    "hola": "¡Hola! ¿Cómo estás?",
    "horario": "Nuestro horario es de 8am a 6pm."
}

def responder_chat(mensaje: str) -> str:
    return respuestas.get(mensaje.lower(), "No entendí tu pregunta.")

