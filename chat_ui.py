# chat_ui.py
import streamlit as st
from chatbot import responder_mensaje

# Inicializar historial y estado
if "historial" not in st.session_state:
    st.session_state.historial = []
if "estado" not in st.session_state:
    st.session_state.estado = {}

# --- CSS para estilo WhatsApp, válido en modo claro y oscuro ---
st.markdown("""
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9; /* fondo claro fijo */
        color: #000000; /* texto negro siempre visible */
    }
    .mensaje {
        margin: 5px;
        padding: 10px 15px;
        border-radius: 20px;
        max-width: 70%;
        word-wrap: break-word;
        color: #000000; /* texto negro en todas las burbujas */
    }
    .usuario {
        background-color: #dcf8c6; /* verde claro tipo WhatsApp */
        align-self: flex-end;
    }
    .bot {
        background-color: #ffffff;
        border: 1px solid #ddd;
        align-self: flex-start;
    }
    </style>
""", unsafe_allow_html=True)

st.title("💬 PorkiBot - Atención al Cliente")

# Campo de entrada
mensaje = st.chat_input("Escribe tu mensaje aquí...")

# Procesar mensaje si existe
if mensaje:
    respuesta = responder_mensaje(mensaje, st.session_state.estado)
    st.session_state.historial.append(("Tú", mensaje))
    st.session_state.historial.append(("PorkiBot", respuesta))

# Mostrar historial
chat_container = st.container()
with chat_container:
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for emisor, texto in st.session_state.historial:
        if emisor == "Tú":
            st.markdown(f"<div class='mensaje usuario'><b>{emisor}:</b> {texto}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='mensaje bot'><b>{emisor}:</b> {texto}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
