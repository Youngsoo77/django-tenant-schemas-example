FROM python:3.6.3

ENV PYTHONUNBUFFERED 1

ADD django_project /app/

WORKDIR  /app/

RUN pip install -r requirements.txt
