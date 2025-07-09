from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow import DAG
from datetime import datetime, timedelta
import pandas as pd
import os

# List of variables used in our code
# We are checking the price of the pound against other major currencies
# This can be changed for any other currency (USD, EUR etc.)
currency = 'GBP'
postgres_conn_id = 'postgres_default'
api_conn_id = 'frankfurter_api'

# The way Airflow works is that it schedules DAG runs based on the
# end of an interval, not the start. So it needs to be set for the day before
default_args = {
    'owner': 'airflow',
    'start_date': datetime.now() - timedelta(days=1)
}

# DAG
# A collection of tasks
# Set the schedule, so it runs each day
with DAG(
        dag_id='exr_etl_pipeline',
        default_args=default_args,
        schedule='@daily',
        catchup=False,
) as dag:
    @task()
    def extract_exr_data():  # First task that extracts data from an API
        # Use HTTP Hook to get connection details from Airflow
        http_hook = HttpHook(http_conn_id=api_conn_id,
                             method='GET')

        # Build the API endpoint
        endpoint = f'/v1/latest?base={currency}'

        response = http_hook.run(endpoint)

        # Checks to see if we can connect to the API
        if response.status_code == 200:
            # Returns the JSON file
            return response.json()
        else:
            raise Exception(f"Failed to fetch exr data: {response.status_code}")


    @task()
    def transform_exr_data(exr_data):
        # Second task uploads the data we want to our own dict
        transformed_data = {
            'amount': exr_data['amount'],
            'base': exr_data['base'],
            'date': exr_data['date'],
            'EUR': exr_data['rates']['EUR'],
            'USD': exr_data['rates']['USD'],
            'AUD': exr_data['rates']['AUD'],
            'JPY': exr_data['rates']['JPY']
        }
        return transformed_data


    @task
    def load_exr_data(transformed_data):
        # Converting the dict to a dataframe for conversion to csv
        new_df = pd.DataFrame([transformed_data])

        # CSV location
        # I have to locate the file in a strange way as this doesn't run
        # on my local machine, it runs through docker
        dag_folder = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(dag_folder, "exr_data.csv")

        # Loads the old data if it exists
        if os.path.isfile(csv_path):
            old_df = pd.read_csv(csv_path)
        else:
            old_df = pd.DataFrame()

        # Concatenate and write back
        full_df = pd.concat([old_df, new_df], ignore_index=True)
        full_df.to_csv(csv_path, index=False, encoding="utf-8")

        # Establish the postgres connection
        pg_hook = PostgresHook(postgres_conn_id=postgres_conn_id)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Creating and inserting into a postgres database
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS exr_data(
            amount money,
            base varchar(3),
            date DATE,
            EUR money,
            USD money,
            AUD money,
            JPY money,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        INSERT INTO exr_data (amount, base, date, EUR, USD, AUD, JPY)
        values (%s, %s, %s, %s, %s, %s, %s)
        """, (
            transformed_data['amount'],
            transformed_data['base'],
            transformed_data['date'],
            transformed_data['EUR'],
            transformed_data['USD'],
            transformed_data['AUD'],
            transformed_data['JPY']
        ))

        conn.commit()
        cursor.close()

    # The schedule
    exr_data = extract_exr_data()
    transformed_data = transform_exr_data(exr_data)
    load_exr_data(transformed_data)
