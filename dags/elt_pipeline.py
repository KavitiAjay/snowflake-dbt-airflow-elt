"""Airflow DAG that runs the dbt project through Cosmos.

Each dbt model becomes its own Airflow task so lineage and selective retries work. Requires an
Airflow Snowflake connection named 'snowflake_default'.
"""

from datetime import datetime
from pathlib import Path

from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from cosmos.profiles import SnowflakeUserPasswordProfileMapping

DBT_PROJECT = Path("/usr/local/airflow/dags/dbt")

profile_config = ProfileConfig(
    profile_name="elt",
    target_name="dev",
    profile_mapping=SnowflakeUserPasswordProfileMapping(
        conn_id="snowflake_default",
        profile_args={"database": "ANALYTICS", "schema": "ELT"},
    ),
)

elt_pipeline = DbtDag(
    project_config=ProjectConfig(DBT_PROJECT),
    profile_config=profile_config,
    execution_config=ExecutionConfig(dbt_executable_path="dbt"),
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dag_id="elt_pipeline",
    tags=["dbt", "snowflake", "tpch"],
)
