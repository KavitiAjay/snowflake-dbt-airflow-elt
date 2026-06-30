# Modern ELT: Snowflake + dbt + Airflow

An end to end ELT pipeline on the TPCH sample data. Airflow orchestrates dbt through Cosmos so
each dbt model shows up as its own Airflow task with real lineage, not one opaque bash step.
Transformations follow a medallion layout (staging, intermediate, marts) and ship with dbt
tests and a Type 2 SCD snapshot.

## Stack

Snowflake, dbt Core, Apache Airflow, Astronomer Cosmos, Docker, GitHub Actions.

## Layers

1. Staging. Light renames and typing over the raw TPCH tables.
2. Marts. Curated fact and dimension tables for analytics.
3. Snapshot. A Type 2 slowly changing dimension on customers so history is preserved.

## Run it locally

1. Install the Astro CLI and Docker Desktop.
2. Put your Snowflake credentials in `.env`.
3. `astro dev start` and open the Airflow UI at localhost:8080.
4. Trigger the `elt_pipeline` DAG. Each dbt model appears as a task group.

## What to highlight in interviews

Cosmos renders the dbt DAG inside Airflow, so a failed test stops exactly the downstream models
that depend on it instead of failing the whole run. That is the difference between scheduling
dbt and orchestrating it.
