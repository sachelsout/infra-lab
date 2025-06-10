# Use an official Python image
FROM python:3.10

# Set working directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

# Expose port and run the app
EXPOSE 5000
CMD ["python", "app.py"]
