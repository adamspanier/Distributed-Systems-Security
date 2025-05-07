# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy the local Python script and requirements.txt into the container
COPY encrypted_populate_data.py /app/populate_data.py
COPY requirements.txt /app/requirements.txt

# Install required packages and system dependencies
RUN apt-get update && \
    apt-get install -y curl && \
    pip install --no-cache-dir -r requirements.txt

# Copy the script
COPY encrypted_populate_data.py .

# Run the traffic generation script
CMD ["python", "populate_data.py"]
