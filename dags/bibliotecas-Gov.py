from airflow.operators.bash_operator import BashOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime
from airflow import DAG
from airflow.operators.python import BranchPythonOperator




def bibliotecas():
    return 'install_tqdm'


with DAG('bibliotecas', start_date=datetime(2022,12,16),
    schedule_interval=None, catchup= False, tags=['Bibliotecas']) as dag:


    taskbibioteca = BranchPythonOperator(
        task_id = 'func_biblioteca',
        python_callable = bibliotecas
    )

    install_pandas = BashOperator(
        task_id='install_tqdm',
        bash_command='pip install tqdm',   
    )

    fim =  DummyOperator(task_id = "fim")

taskbibioteca >> fim