# Use a lightweight Python image
FROM python:3.10.12-slim-buster

# Add maintainer info
LABEL maintainer="Arvind A <pingarvindforquestions>"
LABEL version="1.0"
LABEL description="Dockerfile for the FastAPI app"


# Set the working directory inside the container
WORKDIR /logs-api

# Copy the application code and requirements file to the container
COPY ./app /logs-api/app
COPY ./requirements.txt /logs-api/requirements.txt
COPY ./commands /logs-api/commands

# Create a virtual environment and install dependencies
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --upgrade pip
RUN pip install -r /logs-api/requirements.txt

# Make the entrypoint script executable
RUN chmod +x /logs-api/commands/entrypoint.sh

# Set the command to run when the container starts
CMD ["/logs-api/commands/entrypoint.sh"]