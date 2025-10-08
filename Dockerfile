# Use a more stable base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy only requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose the Render port
EXPOSE 10000

# Command to run the app
CMD ["python", "app.py"]
