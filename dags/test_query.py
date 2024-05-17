
from airflow.decorators import dag, task
from pendulum import datetime
from duckdb_provider.hooks.duckdb_hook import DuckDBHook

DUCKDB_CONN_ID = "duckdb_conn"
DUCKDB_TABLE_NAME = "stocks"

@dag(start_date=datetime(2024, 5, 1), schedule=None, 
     catchup=False, tags=["data-exist-in-db"])

def test_duckdb():
    @task
    def query_duckdb(my_table, conn_id):
        my_duck_hook = DuckDBHook.get_hook(conn_id)
        conn = my_duck_hook.get_conn()

        data = conn.execute(f"SELECT * FROM {my_table};").fetchall()
        return data

    query_duckdb(my_table=DUCKDB_TABLE_NAME, conn_id=DUCKDB_CONN_ID)


test_duckdb()