from airflow.operators.bash_operator import BashOperator
from airflow.decorators import dag, task


@dag(
    schedule_interval=None,
    catchup=False,
    tags=['BIBLIOTECAS'])

def bibliotecas():
    pass
install_pandas = BashOperator(
    task_id='install_tqdm',
    bash_command='pip install tqdm',   
)




install_pandas