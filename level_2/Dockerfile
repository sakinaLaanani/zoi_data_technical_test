FROM python:3.11-slim-buster

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/requirements.txt

RUN pip3 install -r requirements.txt

COPY . /usr/src/app/