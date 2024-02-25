import streamlit as st
from google.oauth2 import service_account
from google.cloud import bigquery
import pandas as pd
from queries import get_streamlit_pypi_data


@st.cache_resource
def get_bigquery_client() -> bigquery.Client:
    credentials = service_account.Credentials.from_service_account_info(
    st.secrets['bigquery_service_account']
    )
    client = bigquery.Client(credentials=credentials)
    return client

client = get_bigquery_client()


@st.cache_data
def get_df_from_sql(query: str) -> pd.DataFrame:
    df = client.query(query).to_dataframe()
    return df


st.title('BigQuery App')
days_lookback = st.slider('Cuantos días de información quieres ver ?',
                            min_value=1, max_value=30, value=5)

query = get_streamlit_pypi_data(days_lookback)

downloads_df = get_df_from_sql(query)

st.line_chart(downloads_df,
                x='file_downloads_timestamp_date',
                y='file_downloads_count')
st.write(downloads_df)