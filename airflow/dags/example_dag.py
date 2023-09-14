from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.databricks.operators.databricks import DatabricksSubmitRunOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'example_databricks_operator',
    default_args=default_args,
    description='An example DAG demonstrating the usage of DatabricksSubmitRunOperator',
    schedule_interval='* 00 * * *',
    start_date=datetime(2023, 1, 1),
    catchup=False,
)

notebook_task = DatabricksSubmitRunOperator(
    task_id='notebook_task',
    new_cluster={
        'spark_version': '8.3.x-scala2.12',
        'node_type_id': 'i3.xlarge',
        'num_workers': 8
    },
    notebook_task={
        'notebook_path': '/Workspace/Path/To/Your/Notebook',
    },
    dag=dag,
)
