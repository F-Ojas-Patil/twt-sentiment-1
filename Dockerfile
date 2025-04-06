# Use an official Python runtime as a base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port your Flask app will run on
EXPOSE 5020

# Define environment variables to prevent Python from writing pyc files to disk
ENV PYTHONUNBUFFERED 1

# Command to run the Flask app
CMD ["python", "app.py"]
