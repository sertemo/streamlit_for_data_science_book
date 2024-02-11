import pandas as pd
import streamlit as st
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

st.title("SF Trees")
st.write(
    "This app analyses trees in San Francisco using"
    " a dataset kindly provided by SF DPW"
)
trees_df = pd.read_csv("trees.csv")
trees_df.dropna(subset=['longitude', 'latitude'], inplace=True)
trees_df = trees_df.sample(1000)
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id']).reset_index()
df_dbh_grouped.columns = ['dbh', 'tree_count']
st.line_chart(df_dbh_grouped)
# Añadimos nueva columna random
df_dbh_grouped['new_col'] = np.random.randn(len(df_dbh_grouped)) * 500
df_dbh_grouped
st.line_chart(df_dbh_grouped, x='dbh', y='tree_count')

st.bar_chart(df_dbh_grouped)
st.area_chart(df_dbh_grouped)

# maps
st.subheader('Maps')
st.map(trees_df)

st.subheader('Plotly Chart')
trees_df = pd.read_csv('trees.csv')
fig = px.histogram(trees_df['dbh'])
st.plotly_chart(fig)

# Seaborn y matplotlib
trees_df['age'] = (pd.to_datetime('today') -
                    pd.to_datetime(trees_df['date'])).dt.days
st.subheader('Seaborn Chart')
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(trees_df['age'])
plt.xlabel('Age ( Days)')
st.pyplot(fig_sb)
st.subheader('Matplotlib Chart')
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(trees_df['age'])
plt.xlabel('Age ( Days)')
st.pyplot(fig_mpl)

st.write(pd.to_datetime('today').strftime('%Y-%m-%d %H:%M:%S'))
st.write(dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

from bokeh.plotting import figure

st.subheader('Bokeh Chart')
scatterplot = figure(title= 'Bokeh Scatterplot')
scatterplot.scatter(trees_df['dbh'], trees_df['site_order'])
scatterplot.yaxis.axis_label = 'site_order'
scatterplot.xaxis.axis_label = 'dbh'
st.bokeh_chart(scatterplot)

import altair as alt

st.subheader('Altair Chart')
df_caretaker = trees_df.groupby(['caretaker']).count()['tree_id'].reset_index()
df_caretaker.columns = ['caretaker', 'tree_count']
fig = alt.Chart(df_caretaker).mark_bar().encode(x='caretaker', y='tree_count')
st.altair_chart(fig)

# Otra opción
fig = alt.Chart(trees_df).mark_bar().encode(x='caretaker', y='count(*):Q')
st.altair_chart(fig)

# Pydeck para geolocalización
import pydeck as pdk
# Tenemos que quitar los nulls cuando queramos usar pydeck
trees_df = pd.read_csv('trees.csv')
trees_df.dropna(how='any', inplace=True)
trees_df.columns
sf_initial_view = pdk.ViewState(
    latitude=37.77,
    longitude=-122.4,
    zoom=11,
)
# Creamos una layer
sp_layer = pdk.Layer(
    'ScatterplotLayer',
    data=trees_df,
    get_position=['longitude', 'latitude'],
    get_radius=30,
    auto_highlight=True,
    pickable=True,
)
#Creamos otra layer
hx_layer = pdk.Layer(
    'HexagonLayer',
    data=trees_df,
    get_position=['longitude', 'latitude'],
    radius=100,
    extruded=True,
)
st.pydeck_chart(pdk.Deck(
    initial_view_state=sf_initial_view,
    map_style='mapbox://styles/mapbox/light-v9',
    layers=[sp_layer, hx_layer]
))