import streamlit as st
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(layout='wide')

st.title("SF Trees")
st.write(
    """
    This app analyses trees in SF using
    a dataset kindly provided by SF DPW
    """
)

trees_df = pd.read_csv("trees.csv")
today = pd.to_datetime('today')
trees_df['date'] = pd.to_datetime(trees_df['date'])
trees_df['age'] = (today - trees_df['date']).dt.days
df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']

col1, col2, col3 = st.columns(3, gap='large')

with col1:
    st.line_chart(df_dbh_grouped, use_container_width=True)

with col2:
    st.bar_chart(df_dbh_grouped)

with col3:
    st.area_chart(df_dbh_grouped)

tab1, tab2, tab3 = st.tabs(['Line Chart', 'Bar Chart', 'Area Chart'])

with tab1:
    st.line_chart(df_dbh_grouped, use_container_width=True)

with tab2:
    st.bar_chart(df_dbh_grouped)

with tab3:
    st.area_chart(df_dbh_grouped)

with st.sidebar:
    graph_color = st.color_picker('Graph Colors', value='#F8B195')
    owners = st.multiselect(
        "Tree Owner Filter",
        trees_df['caretaker'].unique()
    )
    if owners:
        trees_df = trees_df[trees_df['caretaker'].isin(owners)]

df_dbh_grouped = pd.DataFrame(trees_df.groupby(['dbh']).count()['tree_id'])
df_dbh_grouped.columns = ['tree_count']
st.line_chart(df_dbh_grouped)

col1, col2 = st.columns(2)

with col1:
    fig = px.histogram(
        trees_df, 
        x=trees_df['dbh'], 
        title='Tree Width',
        color_discrete_sequence=[graph_color])
    fig.update_xaxes(title_text='Width')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.histogram(
        trees_df, 
        trees_df['age'],
        title='Tree Age',
        color_discrete_sequence=[graph_color]
    )
    st.plotly_chart(fig, use_container_width=True)

