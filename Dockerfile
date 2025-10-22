# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy everything from the current directory to /app in the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port Django will use
EXPOSE 8000

# Run the Django app with Gunicorn
CMD ["gunicorn", "todo_root.wsgi:application", "--bind", "0.0.0.0:8000"]
