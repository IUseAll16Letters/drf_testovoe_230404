FROM python:3.11.2-alpine3.16

COPY requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev

RUN pip install -r requirements.txt --no-cache-dir

RUN adduser --disabled-password django

USER django

