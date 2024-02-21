import pandas as pd
import plotly.express as px
import streamlit as st
from pandas_profiling import ProfileReport
import requests
from streamlit_plotly_events import plotly_events
from streamlit_lottie import st_lottie
from streamlit_pandas_profiling import st_profile_report

def load_lottieurl(url: str) -> dict | None:
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_penguin = load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_lntyk83o.json')

st_lottie(lottie_penguin, height=400, speed=2)

st.title('Streamlit Plotly Events Example + Lottie Example: Penguins')
df = pd.read_csv('penguins.csv')
fig = px.scatter(df, x='bill_length_mm', y='bill_depth_mm', color='species')
selected_point = plotly_events(fig, click_event=True)

penguin_profile = ProfileReport(df, explorative=True)
st_profile_report(penguin_profile)

if len(selected_point) == 0:
    st.stop()

selected_x_value = selected_point[0]['x']
selected_y_value = selected_point[0]['y']
df_selected = df[
    (df['bill_length_mm'] == selected_x_value)
    &
    (df['bill_depth_mm'] == selected_y_value)
]
st.write('Selected point:')
st.write(df_selected)