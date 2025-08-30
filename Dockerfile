FROM python:3.11-slim

WORKDIR /app

# Copy and install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY autoscaler_app.py .

EXPOSE 8000

CMD ["uvicorn", "autoscaler_app:app", "--host", "0.0.0.0", "--port", "8000"]
