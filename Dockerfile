FROM python:3.9-slim-buster

# Create a non-root user and switch to that user
RUN groupadd -r myuser && useradd -r -g myuser myuser

# Set working directory
WORKDIR /app

# Copy the requirements file first (for caching purposes)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Switch to the non-root user
USER myuser

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
