FROM python:3.6-slim

WORKDIR /home/demo/ml_demo

ADD ./src/new_main.py /home/demo/ml_demo/

RUN pip install flask

CMD ["python","new_main.py"]
