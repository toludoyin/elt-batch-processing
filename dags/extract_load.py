
from airflow import Dataset
from airflow.decorators import dag, task
from pendulum import datetime
import requests
import pandas as pd
import re
import duckdb


@dag(
    start_date=datetime(2024, 5, 1),
    schedule= "0 0 * * 6",
    catchup=False,
)

def extract_load_dag():

    @task
    def extract_api_data():
        outlets=[Dataset("stocks_db")]
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=IBM&outputsize=full&apikey=demo'
        api_data = requests.get(url)
        return api_data.json()["Time Series (Daily)"]

    @task
    def load_to_duckdb(data):
        stocks_data = pd.DataFrame(data).T
        stocks_data.reset_index(inplace=True)
        stocks_data.columns = [re.sub(r'[^a-zA-Z]', '', col) for col in stocks_data.columns]

        con = duckdb.connect("stocks_db.db")
        con.execute("CREATE TABLE IF NOT EXISTS stocks AS SELECT * FROM stocks_data")
        con.execute("INSERT INTO stocks SELECT * FROM stocks_data") 
            
    data_from_api = extract_api_data()
    load_to_duckdb(data_from_api)
    
extract_load_dag()