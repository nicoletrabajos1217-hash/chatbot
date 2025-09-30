import streamlit as st
from chatbot import responder_mensaje

# Configuración inicial de la app
st.set_page_config(page_title="Asistente Virtual", layout="centered")

# Sidebar con menú
menu = st.sidebar.radio("📌 Menú", ["🏠 Inicio", "ℹ️ Preguntas frecuentes", "🛍️ Productos", "🛠️ Soporte técnico"])

# Inicializar historial si no existe
if "historial" not in st.session_state:
    st.session_state.historial = []

st.title("🤖 Asistente Virtual de Atención al Cliente")

# Mostrar contenido según el menú
if menu == "🏠 Inicio":
    st.subheader("¡Bienvenido!")
    st.write("Este asistente puede ayudarte con preguntas frecuentes, información de productos y soporte técnico.")
    
    # Caja de texto con envío por Enter
    pregunta = st.text_input("Escribe tu mensaje y presiona **Enter**", key="input", on_change=lambda: None)

    if pregunta:
        respuesta = responder_mensaje(pregunta)
        # Guardar en historial
        st.session_state.historial.append(("Tú", pregunta))
        st.session_state.historial.append(("Bot", respuesta))
        # Resetear input después de enviar
        st.session_state.input = ""

    # Mostrar historial invertido (último mensaje arriba)
    if st.session_state.historial:
        st.subheader("💬 Conversación")
        for emisor, mensaje in reversed(st.session_state.historial):
            st.markdown(f"**{emisor}:** {mensaje}")

elif menu == "ℹ️ Preguntas frecuentes":
    st.subheader("Preguntas frecuentes")
    st.write("""
    - ¿Cuáles son los horarios de atención? → De lunes a viernes de 8am a 6pm.
    - ¿Dónde están ubicados? → En la sede principal de la ciudad.
    - ¿Tienen envíos? → Sí, a nivel nacional.
    """)

elif menu == "🛍️ Productos":
    st.subheader("Nuestros productos")
    productos = {
        "🍲 Sopas": "Producto A: una rica sopa a 5,000",
        "👕 Camisetas": "Camisetas de todas las tallas",
        "🏍️ Motos": "Gran variedad de motos",
        "🍔 Hamburguesa": "Hamburguesa doble carne por 13,000",
        "🎒 Maletas": "Maletas de todas las tallas"
    }
    for nombre, descripcion in productos.items():
        st.markdown(f"**{nombre}** → {descripcion}")

elif menu == "🛠️ Soporte técnico":
    st.subheader("Centro de soporte")
    st.write("¿Tienes problemas con un producto o servicio? Escríbenos en el chat de inicio y nuestro asistente te ayudará.")
