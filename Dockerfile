FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY /app /app

RUN apt-get update && apt-get install -y vim

RUN pip install flask_sqlalchemy
RUN pip install flask_migrate
RUN pip install flask-marshmallow
RUN pip install marshmallow-sqlalchemy 