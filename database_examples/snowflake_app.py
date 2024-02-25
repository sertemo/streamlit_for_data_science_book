import snowflake.connector
from snowflake.connector import SnowflakeConnection
import pandas as pd
import streamlit as st

@st.cache_resource
def init_snowflake() -> SnowflakeConnection:
    session = snowflake.connector.connect(
        **st.secrets['snowflake'],
        client_session_keep_alive=True
    )
    return session

session = init_snowflake()


def run_query(session: SnowflakeConnection,
                sql_query: str) -> pd.DataFrame:
    df = session.cursor().execute(sql_query).fetch_pandas_all()
    return df

sql_query = """
            SELECT
            l_returnflag,
            sum(l_quantity) as sum_qty,
            sum(l_extendedprice) as sum_base_price
            FROM
            snowflake_sample_data.tpch_sf1.lineitem
            WHERE
            l_shipdate <= dateadd(day, -90, to_date('1998-12-01'))
            GROUP BY 1"""

df = run_query(session, sql_query)

st.title('SnowFlake TPC-H Explorer')
col_to_graph = st.selectbox(
    'Selecciona una columna del grafico',
    ['Order Quantity', 'Base Price']
)
df['SUM_QTY'] = df['SUM_QTY'].astype('float32')
df['SUM_BASE_PRICE'] = df['SUM_BASE_PRICE'].astype('float32')

if col_to_graph == 'Order Quantity':
    st.bar_chart(
        data=df,
        x='L_RETURNFLAG',
        y='SUM_QTY'
    )
else:
    st.bar_chart(
        data=df,
        x='L_RETURNFLAG',
        y='SUM_BASE_PRICE'
    )
