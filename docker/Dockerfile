# Use lightweight Python base
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY ../requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the API code and model into the container
COPY ../src/inference ./inference

# Expose the API port
EXPOSE 8000

# Run the FastAPI app
CMD ["uvicorn", "inference.app:app", "--host", "0.0.0.0", "--port", "8000"]
