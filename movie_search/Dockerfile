# Use the official Python 3.12 image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY api/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the api secrets into the container
COPY api/.secrets.toml /app/api/.secrets.toml
COPY api/settings.toml /app/api/settings.toml
# Copy the Django app code into the container
COPY movie_search /app/

# Expose port 8000 for the Django server
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
