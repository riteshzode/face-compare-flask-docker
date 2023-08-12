# Use an official Python runtime as a parent image
FROM python:3.11-slim-buster

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0 libgtk2.0-0 wget

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip3 install -r requirements.txt

# Create .deepface and .deepface/weights directories
RUN mkdir -p /app/.deepface/weights

# Copy the entire data directory into the container's /app/data directory
COPY data /app/data

# Set environment variable to suppress TensorFlow log messages
ENV TF_CPP_MIN_LOG_LEVEL=2

# Copy all files from the current directory into the container at /app
COPY . /app

# Expose port 5000 for Flask app
EXPOSE 5000

# Start the Flask app
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]