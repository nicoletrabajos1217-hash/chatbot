# chatbot.py

# Preguntas frecuentes
faq = {
    "horario": "Nuestro horario de atención es de lunes a viernes de 8:00 a 18:00. Así siempre podrás contactarnos durante el día laboral.",
    "envios": "Los envíos generalmente tardan entre 3 y 5 días hábiles. Si tu pedido es urgente, podemos ofrecer opciones de entrega express.",
    "contacto": "Puedes comunicarte con nosotros por correo soporte@empresa.com o llamando al 123-456-7890. ¡Estamos para ayudarte!",
    "ubicacion": "Nos encontramos en Calle Principal 123, Ciudad Ejemplo. Si deseas, puedo indicarte cómo llegar.",
    "devoluciones": "Aceptamos devoluciones hasta 30 días después de la compra, asegurando que tengas tiempo suficiente para revisar tu pedido."
}

# Productos
productos = {
    "producto sopas": "Nuestra sopa especial se prepara con ingredientes frescos y cuesta 5,000. Perfecta para un almuerzo rápido y delicioso.",
    "producto camiseta": "Disponemos de camisetas de todas las tallas y colores. Ideales para cualquier ocasión o regalo.",
    "producto motos": "Ofrecemos una amplia variedad de motos, desde modelos urbanos hasta deportivos. Te puedo ayudar a elegir según tus necesidades.",
    "producto hamburguesa": "Hamburguesa doble carne por 13,000, con opción de añadir queso extra o vegetales. ¡Una delicia garantizada!",
    "producto maleta": "Maletas de todas las tallas, resistentes y con garantía. Perfectas para tus viajes personales o profesionales."
}

# Soporte técnico
soporte_tecnico = {
    "problema login": "Si no puedes ingresar a tu cuenta, te recomiendo restablecer tu contraseña. Si el problema persiste, puedo guiarte paso a paso.",
    "error pago": "Para problemas de pago, asegúrate de que los datos de tu tarjeta sean correctos. Si continúa, contacta a nuestro soporte para resolverlo rápidamente.",
    "problema app": "Si la aplicación presenta errores, prueba cerrarla y abrirla nuevamente o actualizar a la última versión disponible.",
    "otros": "Por favor describe con detalle tu problema y haré todo lo posible para ofrecerte una solución rápida y efectiva."
}

# Función principal para responder
def responder_mensaje(texto):
    texto = texto.lower().strip()

    # Saludos
    if any(palabra in texto for palabra in ["hola", "buenas", "hi", "hey"]):
        return "¡Hola! Encantado de saludarte. Soy tu asistente virtual y puedo ayudarte con preguntas sobre nuestros productos, envíos o soporte técnico. ¿Por dónde quieres empezar?"
    
    if any(palabra in texto for palabra in ["adiós", "chao", "bye"]):
        return "¡Hasta luego! Espero haber resuelto tus dudas. Si necesitas algo más, siempre puedes escribirme nuevamente."

    # Revisar FAQ
    for clave, respuesta in faq.items():
        if clave in texto:
            return respuesta

    # Revisar productos
    for clave, info in productos.items():
        if clave in texto:
            return info

    # Revisar soporte técnico
    for clave, ayuda in soporte_tecnico.items():
        if clave in texto:
            return ayuda

    # Respuesta por defecto creativa
    return f"Interesante pregunta sobre '{texto}'. Aún no tengo una respuesta exacta, pero puedo ayudarte con nuestras FAQs, productos o soporte técnico. ¿Cuál de estos te interesa explorar primero?"

