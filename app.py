from fastapi import FastAPI
from chatbot import responder_chat

app = FastAPI()

@app.get("/chat/{mensaje}")
def responder(mensaje: str):
    return {"respuesta": responder_chat(mensaje)}
