# cURL & Python Foundations Dockerfile
FROM python:3.8-alpine

RUN apk add curl && \
    mkdir /development

WORKDIR /development

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install --upgrade pip

LABEL \
    maintainer='Tim Hull <tim.hull@wwt.com>' \
    version='1.0'

CMD sh