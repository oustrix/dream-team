FROM python:3.11.4-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./.env ./.env

CMD python -m src.market
