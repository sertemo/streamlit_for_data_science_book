import pandas as pd
import streamlit as st
from streamlit_folium import st_folium
import folium

st.title('SF Trees Map')
trees_df = pd.read_csv('trees.csv')
trees_df = trees_df.dropna(subset=['longitude', 'latitude'])
trees_df = trees_df.head(n=100)
lat_avg = trees_df['latitude'].mean()
lon_avg = trees_df['longitude'].mean()

m = folium.Map(
    location=[lat_avg, lon_avg],
    zoom_start=12
)

for _, row in trees_df.iterrows():
    folium.Marker(
        [row['latitude'], row['longitude']],
    ).add_to(m)
events = st_folium(m)

if events:
    lat_clicked = events['last_object_clicked']['lat']
    lon_clicked = events['last_object_clicked']['lng']
    clicked_df = trees_df[
        (trees_df['longitude'] == lon_clicked)
        &
        (trees_df['latitude'] == lat_clicked)
    ]
    st.write(clicked_df)