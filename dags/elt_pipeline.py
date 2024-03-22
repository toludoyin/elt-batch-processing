import requests
import pandas as pd
import re
import duckdb 


def extract_api_data():
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=TSCO.LON&outputsize=full&apikey=demo'
    api_data = requests.get(url)
    return api_data.json()["Time Series (Daily)"]

def load_to_duckdb(data):
    stocks_data = pd.DataFrame(data).T
    stocks_data.reset_index(inplace=True)
    stocks_data.rename(columns = {'index' : 'date'}, inplace=True)
    stocks_data.columns = [re.sub(r'[^a-zA-Z]', '', col) for col in stocks_data.columns]
    
    con = duckdb.connect("stocks_db.db")
    con.execute("CREATE TABLE IF NOT EXISTS stocks_db AS SELECT * FROM 'stocks_data'")
    con.execute("INSERT INTO stocks_db SELECT * FROM stocks_data") 
    con.sql("SELECT * from stocks_db").show()

data_from_api = extract_api_data()
load_to_db = load_to_duckdb(data_from_api)