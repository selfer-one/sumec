FROM python:3.13-slim

WORKDIR /app

COPY main.py .
COPY test.py .

CMD ["python", "main.py"]
