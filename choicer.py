import streamlit as st
import pandas as pd
from typing import Awaitable
import asyncio
from openai import OpenAI
from openai import AsyncOpenAI
import json

def append_message(conversation : list[str], content : str, role : str) -> list[str]:
    conversation.append({"role": role, "content": content})
    return conversation

async def get_prompt(conversation : list[str]) -> Awaitable[str]:
    completion = await st.session_state.asyn.chat.completions.create(model="gpt-3.5-turbo", messages=conversation)
    return completion

def get_last_message(role : str) -> str:
    messages = list(filter(lambda x: x["role"] == role, st.session_state.conversation))
    return messages[len(messages)-1]["content"]

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

with open("./conf/prompts.json") as f:
    prompts = json.load(f)

with open("./conf/text.json") as f:
    text = json.load(f)

with open("./conf/conf.json") as f:
    conf = json.load(f)

# Configuración del título de la página
st.title("Choicer!!")

# Creación de un sidebar
st.sidebar.header("Opciones")

# Añadir elementos al sidebar
opcion_1 = st.sidebar.checkbox("Mostrar información adicional")

# Texto en la página principal
st.write("""
Esta es una aplicación básica de Streamlit. Puedes personalizarla según tus necesidades.
""")

if 'first_run' not in st.session_state:
    st.session_state.first_run = 1
    st.session_state.asyn = AsyncOpenAI(api_key=conf.get("openai_api_key"))
    st.session_state.conversation = append_message(
            st.session_state.conversation, 
            prompts.get("prompt1"), 
            "user"
        )
    completion = asyncio.run(
        get_prompt(st.session_state.conversation))
    st.session_state.conversation  = append_message(
            st.session_state.conversation,
            completion.model_dump()['choices'][0]['message']["content"],
            "assistant"
        )
input = st.text_area(
    "¿Qué terrible decisión aqueja a su excelencia hoy?", "...", height=100)

if st.button("Actualizar resultados"):
    if input:
    # Realiza la llamada al API de OpenAI para generar texto
        st.session_state.conversation = append_message(
            st.session_state.conversation, 
            f"{prompts.get('prompt2')} {input}", 
            "user"
        )
        completion = asyncio.run(
            get_prompt(st.session_state.conversation))
        st.session_state.conversation  = append_message(
            st.session_state.conversation,
            completion.model_dump()['choices'][0]['message']["content"],
            "assistant"
        )
        st.write("Sus resultados:")
        st.markdown(get_last_message("assistant"), unsafe_allow_html=True)
    else:
        st.warning("Por favor, ingresa un prompt antes de generar texto.")