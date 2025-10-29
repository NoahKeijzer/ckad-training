FROM python:3.13-slim

WORKDIR /app

# Copy your project (including pyproject.toml)
COPY . /app

# Install system dependencies for building packages like psycopg2
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev postgresql-client \
    && python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir .[dev] \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

# Expose FastAPI port
EXPOSE 8000

# Run your app with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
