import streamlit as st
import altair as alt
import pandas as pd
import seaborn as sns
import time

st.title("Palmer's Penguins")
st.markdown("Use this Streamlit app to make your own scatterplot about penguins!")

penguin_file = st.file_uploader("Select your local Penguin CSV")

@st.cache_data()
def load_file(penguin_file):
    with st.empty():
        st.write("esperando...")
        time.sleep(3)
        st.write("")

    if penguin_file is not None:
        df = pd.read_csv(penguin_file)
    else:
        df = pd.read_csv('penguins.csv')
    return df

penguins_df = load_file(penguin_file)
# selected_species = st.selectbox('Qué especies quiere visualizar ?', ['Adelie', 'Gentoo', 'Chinstrap'])
selected_x_var = st.selectbox(
    "What do you want the x variable to be?",
    ["bill_length_mm", "bill_depth_mm", "flipper_length_mm", "body_mass_g"],
)
selected_y_var = st.selectbox(
    "What about the y?",
    ["bill_depth_mm", "bill_length_mm", "flipper_length_mm", "body_mass_g"],
)
selected_gender = st.selectbox(
    "Qué género quieres filtrar?",
    ['all penguins', 'male penguins', 'female penguins'],
)

if selected_gender == 'male penguins':
    penguins_df = penguins_df[penguins_df.sex == 'male']
elif selected_gender == 'female penguins':
    penguins_df = penguins_df[penguins_df.sex == 'female']
else:
    pass


alt_chart = (
    alt.Chart(penguins_df, title=f"Scatterplot of Palmers Penguins with {selected_gender}")
    .mark_circle()
    .encode(
        x=selected_x_var,
        y=selected_y_var,
        color='species'
    )
    .interactive()
)
st.altair_chart(alt_chart, use_container_width=True)