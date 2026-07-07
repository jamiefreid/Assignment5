# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy app files
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port Flask runs on
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]