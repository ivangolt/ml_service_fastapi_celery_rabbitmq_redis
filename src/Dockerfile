# Service API app
FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --no-cache-dir poetry
RUN poetry install --no-interaction

COPY . /app/src/