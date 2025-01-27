### elt-batch-processing

ELT batch processing, extract data from stocks API into *duckdb* database, transformed the data with *dbt* and *airflow* to ochestrate the workflow.

Setup:

Without airflow

* Create a virtual environment

* Install DuckDB and connector dbt-duckdb

* Extract data from API into DuckDB

* Create dbt project

* Initialize dbt with `dbt init`

* Use `dbt debug` to test connections

With airflow

* Use the `astro dev init` - to setup airflow

* Install dependencies

* Start airflow using `astro dev start`  
