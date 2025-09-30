# chat_ui.py
import streamlit as st
from chatbot import responder_mensaje

# Inicializar historial y estado
if "historial" not in st.session_state:
    st.session_state.historial = []
if "estado" not in st.session_state:
    st.session_state.estado = {}

# --- CSS para estilo tipo WhatsApp ---
st.markdown("""
    <style>
    .chat-container {
        display: flex;
        flex-direction: column; /* mensajes en orden normal */
        max-height: 500px;
        overflow-y: auto; /* scroll interno */
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .mensaje {
        margin: 5px;
        padding: 10px 15px;
        border-radius: 20px;
        max-width: 70%;
        word-wrap: break-word;
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

# Mostrar historial en orden normal (lo nuevo abajo)
chat_container = st.container()
with chat_container:
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for emisor, texto in st.session_state.historial:
        if emisor == "Tú":
            st.markdown(f"<div class='mensaje usuario'><b>{emisor}:</b> {texto}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='mensaje bot'><b>{emisor}:</b> {texto}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

# --- Autoscroll al último mensaje ---
if st.session_state.historial:
    last_msg = st.session_state.historial[-1][1]
    st.markdown(f"<div style='height:1px;' id='scroll'></div>", unsafe_allow_html=True)
    st.markdown(
        """
        <script>
        var el = document.getElementById("scroll");
        if (el) { el.scrollIntoView({behavior: "smooth", block: "end"}); }
        </script>
        """,
        unsafe_allow_html=True,
    )
