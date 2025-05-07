FROM python:3.11-slim

WORKDIR /app

COPY test_runner.py .

RUN pip install --no-cache-dir --upgrade pip

CMD ["python", "test_runner.py"]
