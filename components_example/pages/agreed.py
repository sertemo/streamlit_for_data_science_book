import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

st.title('Streamlit AgGrid Example: Penguins')
penguins_df = pd.read_csv('penguins.csv')
st.write('AgGrid DataFrame:')
response = AgGrid(penguins_df, editable=True, height=500)
df_edited = response['data']
st.write('Edited DataFrame:')
st.dataframe(df_edited)