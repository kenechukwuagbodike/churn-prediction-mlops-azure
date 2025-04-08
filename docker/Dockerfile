# Use official Python slim image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy source code (only needed for docker build context; compose volumes override this)
COPY ./src /app/src

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Expose ports (optional; Compose already handles it)
EXPOSE 8000
EXPOSE 7860

# Default command (overridden by Compose)
CMD ["uvicorn", "src.inference.app:app", "--host", "0.0.0.0", "--port", "8000"]
