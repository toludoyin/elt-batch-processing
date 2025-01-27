### elt-batch-processing

ELT batch processing, extract data from stocks API into *duckdb* database, transform it using *dbt*, and ochestrate the workflow using *airflow*.

**Setup**:

Without airflow

* Create a virtual environment

* Install DuckDB, dbt-duckdb connector and other dependecies

* Extract data from API into DuckDB

* Create dbt project

* Initialize dbt with `dbt init`

* Configure destination in `profiles.yml` file

* Use `dbt debug` to test connections

* Define models

* Execute trasformation with `dbt run`

* Verify content in database
  

With airflow for orchestration

* Use the `astro dev init` - to setup airflow

* Install dependencies

* Start airflow using `astro dev start`  
