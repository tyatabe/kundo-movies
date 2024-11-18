# Use the official Python 3.12 image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY api/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the search API code into the container
COPY api /app/api

# Set the PYTHONPATH to make the `api` directory discoverable as a module
ENV PYTHONPATH=/app

# Expose port 4000 for the API
EXPOSE 4000

# Run the API server
CMD ["python", "api/app.py"]
