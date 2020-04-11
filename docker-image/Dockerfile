# cURL & Python Foundations Dockerfile
FROM python:3.8-alpine

RUN apk add curl && \
    mkdir /code

WORKDIR /code

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN pip install --upgrade pip

LABEL \
    maintainer='Tim Hull <tim.hull@wwt.com>' \
    version='1.0'

ENV MERAKI_API_KEY="6bec40cf957de430a6f1f2baa056b99a4fac9ea0" \
    DNAC_USER="devnetuser" \
    DNAC_PW="Cisco123!"

CMD sh