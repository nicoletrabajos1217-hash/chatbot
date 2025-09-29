import streamlit as st
from chatbot import responder_mensaje

# Configuración de la app
st.set_page_config(page_title="Chatbot Atención al Cliente", page_icon="🤖")
st.title("Chatbot Profesional de Atención al Cliente")
st.write("¡Hola! Soy tu asistente virtual. Puedo responder preguntas frecuentes, dar información de productos y soporte técnico.")

# Inicializar historial
if "historial" not in st.session_state:
    st.session_state.historial = []

# Entrada de usuario
entrada = st.text_input("Escribe tu mensaje:")

# Botón enviar
if st.button("Enviar") and entrada:
    respuesta = responder_mensaje(entrada)
    st.session_state.historial.append({"usuario": entrada, "chatbot": respuesta})

# Mostrar historial de conversación
for mensaje in st.session_state.historial:
    st.markdown(f"**Tú:** {mensaje['usuario']}")
    st.markdown(f"**Chatbot:** {mensaje['chatbot']}")
    st.markdown("---")
