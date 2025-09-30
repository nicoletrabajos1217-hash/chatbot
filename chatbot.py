# chatbot.py

def responder_mensaje(mensaje, estado):
    mensaje = mensaje.lower().strip()

    # 1. Estado inicial: presentación
    if estado.get("fase") is None:
        estado["fase"] = "inicio"
        return "👋 ¡Hola! Soy PorkiBot, tu asistente virtual de atención al cliente. Antes de continuar, ¿me dices tu nombre?"

    # 2. Guardar nombre
    if estado.get("fase") == "inicio":
        estado["nombre"] = mensaje.capitalize()
        estado["fase"] = "menu"
        return f"Encantado de conocerte, {estado['nombre']} 😃.\n\nEstas son mis opciones:\n- Productos\n- Soporte\n- Preguntas frecuentes\n\n👉 Escribe una opción para continuar."

    # 3. Menú principal
    if estado.get("fase") == "menu":
        if "producto" in mensaje:
            estado["fase"] = "productos"
            return (
                "📦 ¡Genial! Estos son algunos productos disponibles:\n"
                "- Sopa\n"
                "- Camiseta\n"
                "- Moto\n"
                "- Hamburguesa\n"
                "- Maleta\n\n"
                "👉 Dime cuál te interesa o escribe 'menú' para volver."
            )
        elif "soporte" in mensaje:
            estado["fase"] = "soporte"
            return (
                "🛠️ Estás en soporte técnico. ¿Qué problema tienes?\n"
                "- Problemas de acceso\n"
                "- Errores en la plataforma\n"
                "- Otro"
            )
        elif "pregunta" in mensaje or "faq" in mensaje:
            estado["fase"] = "faq"
            return (
                "❓ Preguntas frecuentes:\n"
                "- ¿Cuáles son los horarios de atención?\n"
                "- ¿Dónde están ubicados?\n"
                "- ¿Qué medios de pago aceptan?"
            )
        else:
            return "Por favor elige una opción válida: productos, soporte o preguntas frecuentes."

    # 4. Productos
    if estado.get("fase") == "productos":
        if "sopa" in mensaje:
            return "🍲 Nuestras sopas caseras cuestan desde 5,000. Son ideales para un almuerzo rápido y nutritivo."
        elif "camiseta" in mensaje:
            return "👕 Tenemos camisetas de todas las tallas en algodón premium. Desde 25,000."
        elif "moto" in mensaje:
            return "🏍️ Tenemos motos de baja, media y alta gama. ¿Quieres que te muestre un catálogo?"
        elif "hamburguesa" in mensaje:
            return "🍔 Hamburguesas doble carne desde 13,000. Con opción de papas y gaseosa."
        elif "maleta" in mensaje:
            return "🎒 Maletas resistentes al agua, desde 40,000. Perfectas para viajes."
        elif "menú" in mensaje:
            estado["fase"] = "menu"
            return "Volvamos al menú principal. 👉 Opciones: **productos, soporte, preguntas frecuentes**."
        else:
            return "Puedes pedirme detalles de: sopa, camiseta, moto, hamburguesa o maleta. O escribe 'menú' para volver."

    # 5. Soporte
    if estado.get("fase") == "soporte":
        if "acceso" in mensaje:
            return "🔑 Si tienes problemas de acceso, intenta restablecer tu contraseña. ¿Quieres que te guíe?"
        elif "error" in mensaje:
            return "⚠️ Si ves un error en la plataforma, prueba cerrar sesión y volver a entrar. Si persiste, contacta soporte técnico."
        elif "otro" in mensaje:
            return "Por favor descríbeme tu problema con más detalle."
        elif "menú" in mensaje:
            estado["fase"] = "menu"
            return "Volvemos al menú principal. 👉 Opciones: productos, soporte, preguntas frecuentes."
        else:
            return "Indícame si es problema de acceso, error en la plataforma u otro. O escribe 'menú' para regresar."

    # 6. Preguntas frecuentes
    if estado.get("fase") == "faq":
        if "horario" in mensaje:
            return "🕐 Nuestro horario de atención es de lunes a viernes de 8:00 a 18:00."
        elif "ubic" in mensaje:
            return "📍 Estamos ubicados en el centro de la ciudad, cerca de la plaza principal."
        elif "pago" in mensaje:
            return "💳 Aceptamos pagos en efectivo, tarjeta débito, crédito y transferencias."
        elif "menú" in mensaje:
            estado["fase"] = "menu"
            return "Volvemos al menú principal. 👉 Opciones: productos, soporte, preguntas frecuentes."
        else:
            return "Puedes preguntarme por: horarios, ubicación o medios de pago. O escribe 'menú' para volver."

    # 7. Respuesta genérica
    return "Lo siento, no entendí tu mensaje. Escribe 'menú' para volver al inicio de las opciones."
