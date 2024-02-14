
import streamlit as st
from transformers import pipeline


st.title("Hugging Face Demo")
text = st.text_input('Escribe el texto a analizar')

@st.cache_resource()
def get_hugginface_model() -> None:
    model = pipeline('sentiment-analysis')
    return model
model = get_hugginface_model()
if text:
    result = model(text)
    st.write("Sentiment:", result[0]['label'])
    st.write('Confidence:', result[0]['score'])