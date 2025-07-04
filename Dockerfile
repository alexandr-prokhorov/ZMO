FROM python:3.11-slim

WORKDIR /code

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements_docker.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements_docker.txt

COPY . .

RUN mkdir -p /code/staticfiles /code/media