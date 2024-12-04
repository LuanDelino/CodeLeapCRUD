# Builder
FROM python:3.10.4-slim-buster as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install --no-cache-dir djangorestframework psycopg2 python-dotenv


# Runtime Stage
FROM python:3.10.4-slim-buster

WORKDIR /app

COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

COPY . .
