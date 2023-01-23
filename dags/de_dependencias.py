from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG
from airflow.operators.dummy import DummyOperator
from datetime import datetime

def install_dependencies():
    import subprocess
    subprocess.call(["pip", "install", "tqdm"])

dag = DAG(dag_id="install_dependencies",
    start_date=datetime.now(),
    schedule_interval=None)

inicio =  DummyOperator(task_id = "inicio")
fim =  DummyOperator(task_id = "fim")

install_dependencies_task = PythonOperator(
    task_id="install_dependencies",
    python_callable=install_dependencies,
    dag=dag,
)

inicio >> install_dependencies >> fim

