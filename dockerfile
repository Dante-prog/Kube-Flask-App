FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
COPY .env .

EXPOSE 8080

CMD ["gunicorn","wsgi:app", "-w", "4", "-b", "0.0.0.0:8080"]
