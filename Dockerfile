FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install tqdm
CMD ["python","main.py"]