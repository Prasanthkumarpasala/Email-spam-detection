# Use official Python slim image
FROM python:3.9-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files into container
COPY . .

# Expose port 80 for the Flask app
EXPOSE 80

# Run the app
CMD ["python", "app.py"]


