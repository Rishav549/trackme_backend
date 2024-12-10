FROM python:3.11-slim

# Set the working directory

WORKDIR /app

# Copy the current directory contents into the container at /app

COPY . /app
COPY .env /app/.env


# Install any needed packages specified in requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port the application runs on
EXPOSE 8006

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Run the server
CMD ["python", "main.py"]