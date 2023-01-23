from airflow.operators.dummy import DummyOperator
from datetime import datetime
from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

inicio =  DummyOperator(task_id = "inicio")
fim =  DummyOperator(task_id = "fim")



def install_dependencies():
    import subprocess
    subprocess.call(["pip", "install", "pandas"])

dag = DAG(dag_id="install_dependencies", schedule_interval=None, start_date=datetime.now())

install_dependencies_task = PythonOperator(
    task_id="install_dependencies",
    python_callable=install_dependencies,
    dag=dag,
)


inicio >> install_dependencies >> fim

