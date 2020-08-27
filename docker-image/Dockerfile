# cURL & Python Foundations Dockerfile
FROM python:3.8-alpine

RUN apk add curl && \
    mkdir /code

WORKDIR /code

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt
RUN python -m pip install -r requirements.txt

LABEL \
    maintainer='Tim Hull <tim.hull@wwt.com>' \
    version='1.1'

ENV MERAKI_TOKEN="6bec40cf957de430a6f1f2baa056b99a4fac9ea0" \
    DNAC_USER="devnetuser" \
    DNAC_PW="Cisco123!"

CMD sh