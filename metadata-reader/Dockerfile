FROM python:3.8-slim-buster

WORKDIR /app/
COPY src/ /app/

RUN pip install --upgrade pip \
    && pip install pipenv
RUN pipenv install --skip-lock --system
