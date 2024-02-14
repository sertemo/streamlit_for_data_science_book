from dotenv import load_dotenv
import os
from openai import OpenAI
import streamlit as st
import json

load_dotenv()

st.cache_resource()
def get_client() -> OpenAI:
    return OpenAI(api_key=os.environ['OPENAI_API_KEY'])

st.title("OpenAI Demo")
text = st.text_input('Escribe el texto a analizar')

DEFAULT_SYSTEM_MESSAGE = """Eres un experto analizador de sentimientos de textos.
Siempre respondes con el sentimiento del texto pasado y con un número entre 0 y 1 correspondiente
a la confianza de tu predicción. Devuelve la respuesta en formato json."""

system_message = st.text_area("Escribe el mensaje del sistema", DEFAULT_SYSTEM_MESSAGE, height=150)

analyze_button = st.button("Analizar texto")

client = get_client()
if analyze_button and text:    
    messages = [
        {"role": "system", "content": system_message},
            {"role": "user",
                "content": f"Analiza el sentimiento del siguiente texto: {text}"}
    ]
    with st.spinner("Analizando el texto"):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo-1106",
            messages=messages,
            response_format={'type': 'json_object'}
        )
    sentiment = response.choices[0]. message.content.strip()
    st.subheader("Respuesta")
    st.write(json.loads(sentiment))

