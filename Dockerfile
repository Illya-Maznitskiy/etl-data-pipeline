FROM python:3.11-slim

# Install PostgreSQL client tools
RUN apt-get update && apt-get install -y postgresql-client

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Command to execute when container starts
CMD ["python", "src/load_data.py"]
