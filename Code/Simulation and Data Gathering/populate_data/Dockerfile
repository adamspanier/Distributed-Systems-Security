# Use an official Python image as a base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local Python script and requirements.txt into the container
COPY populate_data.py /app/populate_data.py
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run the Python script when the container starts
CMD ["python", "populate_data.py"]
