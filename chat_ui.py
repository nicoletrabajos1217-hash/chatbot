# chat_ui.py
import streamlit as st
from chatbot import responder_mensaje

# Inicializar historial y estado
if "historial" not in st.session_state:
    st.session_state.historial = []
if "estado" not in st.session_state:
    st.session_state.estado = {}

st.title("💬 PorkiBot - Atención al Cliente")

# Campo de entrada con enter para enviar
mensaje = st.chat_input("Escribe tu mensaje aquí...")

# Procesar mensaje si existe
if mensaje:
    respuesta = responder_mensaje(mensaje, st.session_state.estado)
    st.session_state.historial.append(("Tú", mensaje))
    st.session_state.historial.append(("PorkiBot", respuesta))

# Mostrar historial invertido (lo último aparece primero)
for emisor, texto in reversed(st.session_state.historial):
    if emisor == "Tú":
        st.markdown(f"**👤 {emisor}:** {texto}")
    else:
        st.markdown(f"**🤖 {emisor}:** {texto}")

