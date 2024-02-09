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

st.write(pd.to_datetime('today'))
st.write(dt.datetime.today())