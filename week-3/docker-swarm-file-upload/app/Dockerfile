# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the app port
EXPOSE 8000

# Run the app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:app"]

