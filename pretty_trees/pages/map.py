import streamlit as st
import pandas as pd

st.title('Sf Trees map')
st.write("Trees By location")


trees_df = pd.read_csv("trees.csv")

trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.sample(n=1000, replace=True)
st.map(trees_df)