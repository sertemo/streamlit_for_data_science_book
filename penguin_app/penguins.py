import streamlit as st
import altair as alt
import pandas as pd

st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

penguins_df = pd.read_csv("penguins.csv")

# selected_species = st.selectbox('Qué especies quiere visualizar ?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
)


alt_chart = (
    alt.Chart(penguins_df, title="Scatterplot of Palmers Penguins")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color='species'
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)