#"2.3.0"
FROM apache/airflow:2.3.0
COPY requirements.txt /requirements.t
RUN pip install --user --upgrade pip
RUN pip install -no-cache-dir --user -r /requirements.txt