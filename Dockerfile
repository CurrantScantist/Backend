# syntax=docker/dockerfile:1

FROM python:3.7

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 3333

COPY . .

CMD ["uvicorn", "server.app:app", "--host", "0.0.0.0", "--port", "3333"]