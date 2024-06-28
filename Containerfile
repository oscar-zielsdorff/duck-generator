FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the Python script to the container
COPY script.py /app/script.py

# Create a directory for logs
RUN mkdir -p /app/logs

# Install packages
RUN apt-get update && apt-get install -y \
    tree

# Install dependencies
RUN pip install pillow

# Ensure the script is executable
RUN chmod +x /app/script.py

# Run the Python script
CMD ["python3", "/app/script.py"]
