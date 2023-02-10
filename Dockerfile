FROM python:3.8-slim

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app /app

WORKDIR /app

ENV filepath=""

CMD ["sh", "-c", "python main.py $filepath"]