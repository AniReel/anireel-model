FROM python:3.9

WORKDIR /code 

COPY ./requirements.txt /code/requirements.txt 

RUN pip install --upgrade pip

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./__init__.py /code/__init__.py

COPY ./cred.env /code/cred.env 

COPY ./mini_data.csv /code/mini_data.csv 

COPY ./recommend.py /code/recommend.py 

COPY ./main.py /code/main.py  

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
