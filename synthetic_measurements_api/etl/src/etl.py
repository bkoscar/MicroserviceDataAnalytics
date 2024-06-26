import requests
import pandas as pd
from sqlalchemy import create_engine, types
import os
from dotenv import load_dotenv

class ETL:
    """Clase para manejar el proceso ETL."""

    def __init__(self, api_url):
        self.api_url = api_url

    def extract_data(self):
        """Extrae datos desde la API."""
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Levanta una excepción para códigos 4xx o 5xx
            return response.json()['data']
        except requests.RequestException as e:
            raise SystemExit(e)

    def load_data_to_db(self, data):
        """Carga los datos transformados a la base de datos."""
        # Cargar las variables de entorno
        load_dotenv()
        db_user = os.getenv('POSTGRES_USER')
        db_password = os.getenv('POSTGRES_PASSWORD')
        db_name = os.getenv('POSTGRES_DB')
        db_host = 'db'  # Asumiendo que el host de la base de datos es 'db', ajusta según tu configuración

        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:5432/{db_name}')
        data_df = pd.DataFrame(data)
        data_df.to_sql('sensor_data', con=engine, if_exists='append', index=False, dtype={
            'timestamp': types.TIMESTAMP(),
            'temperature': types.NUMERIC(),
            'humidity': types.NUMERIC(),
            'pressure': types.NUMERIC(),
            'wind_speed': types.NUMERIC(),
            'wind_direction': types.INTEGER(),
            'co2_levels': types.NUMERIC(),
            'luminosity': types.NUMERIC(),
            'failure': types.INTEGER()
        })

    def run(self):
        """Ejecuta el proceso ETL completo."""
        data = self.extract_data()
        self.load_data_to_db(data)
        print("Datos guardados en la base de datos exitosamente.")

if __name__ == "__main__":
    api_url = "http://api:8000/measurements/"
    etl_process = ETL(api_url)
    etl_process.run()