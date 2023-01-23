from airflow.operators.dummy import DummyOperator
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator





def install_dependencies():
    import subprocess
    subprocess.call(["pip", "install", "tqdm"])


with DAG('bibliotecas', start_date=datetime(2022,12,16),
    schedule_interval=None, catchup= False, tags=['Bibliotecas']) as dag:

    install_dependencies_task = PythonOperator(
        task_id="install_dependencies",
        python_callable=install_dependencies
        )

    inicio =  DummyOperator(task_id = "inicio")
    fim =  DummyOperator(task_id = "fim")

inicio >> install_dependencies >> fim