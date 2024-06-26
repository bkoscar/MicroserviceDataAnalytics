import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import streamlit as st
import plotly.express as px


load_dotenv()
# Obtener las variables de entorno para la conexión a la base de datos
db_name = os.getenv('POSTGRES_DB')
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_host = 'synthetic_db_container'  # Este valor parece ser fijo y no depende de una variable de entorno



# Create an SQLAlchemy engine
engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}/{db_name}')

# Use the engine to execute the SQL query and load the result into a DataFrame
query = """
SELECT timestamp, temperature, humidity, pressure, wind_speed, wind_direction, co2_levels, luminosity, failure
FROM sensor_data
ORDER BY timestamp;
"""
data_df = pd.read_sql_query(query, engine)

# Close the SQLAlchemy engine connection
engine.dispose()

# Streamlit title
st.title('Sensor Data Visualization')

# Visualización de los datos con Streamlit
# Seleccionar la variable para visualizar, excluyendo 'failure'
options = ['temperature', 'humidity', 'pressure', 'wind_speed', 'wind_direction', 'co2_levels', 'luminosity']
option = st.selectbox(
    'Which data would you like to visualize?',
    options
)

# Crear la figura con plotly
fig = px.line(data_df, x='timestamp', y=option, title=f'Time vs {option.capitalize()}', labels={option: option.capitalize()})
fig.update_xaxes(rangeslider_visible=True)
fig.update_layout(xaxis=dict(rangeselector=dict(buttons=list([
    dict(count=1, label="1m", step="month", stepmode="backward"),
    dict(count=6, label="6m", step="month", stepmode="backward"),
    dict(count=1, label="YTD", step="year", stepmode="todate"),
    dict(count=1, label="1y", step="year", stepmode="backward"),
    dict(step="all")
]))))

# Mostrar la figura en Streamlit
st.plotly_chart(fig)