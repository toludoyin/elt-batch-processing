
from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from airflow.datasets import Dataset
from datetime import datetime

stocks_dataset = Dataset("duckdb://stocks_db")

profile_config = ProfileConfig(
    profile_name="data_pipeline",
    target_name="dev",
    profiles_yml_filepath="/usr/local/airflow/dbt/data_pipeline/profiles.yml"
)
dbt_task_dag = DbtDag(
    project_config=ProjectConfig("/usr/local/airflow/dbt/data_pipeline"),
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path= "/usr/local/airflow/dbt_venv/bin/dbt"),
    schedule=[stocks_dataset],
    start_date=datetime(2024, 5, 1),
    default_args={"retries": 2},
    dag_id="daily_stocks_dag",
)