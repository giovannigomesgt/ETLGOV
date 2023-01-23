from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

def install_dependencies():
    import subprocess
    subprocess.call(["pip", "install", "tqdm"])

dag = DAG(dag_id="install_dependencies", schedule_interval=None)

install_dependencies_task = PythonOperator(
    task_id="install_dependencies",
    python_callable=install_dependencies,
    dag=dag,
)