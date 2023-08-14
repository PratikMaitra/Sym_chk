# Use an official Python runtime as a base image
FROM python:3.10-slim-buster

# Set the working directory in the docker image
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable to tell Flask to run in production mode
ENV FLASK_ENV=production

# Run the app when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
