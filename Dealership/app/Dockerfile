# Use the official Python image as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app/src  # Adjust this to the correct path

# Install Poetry
RUN pip install poetry

# Copy pyproject.toml and poetry.lock
COPY pyproject.toml poetry.lock* /app/

# Install dependencies
RUN poetry install --no-dev

# Copy the rest of the application code
COPY . /app

CMD python -m uvicorn main:app --host 0.0.0.0 --port 8000