FROM python:3.6-slim

WORKDIR /home/demo/ml_demo

ADD ./main.py /home/demo/ml_demo/

RUN pip install flask

CMD ["python","main.py"]
