FROM python:3.13-slim

WORKDIR /app

COPY . /app

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && if [ -f requirements.txt ]; then python -m pip install --no-cache-dir -r requirements.txt; else python -m pip install --no-cache-dir fastapi uvicorn[standard]; fi \
    && apt-get purge -y --auto-remove build-essential \
    && rm -rf /var/lib/apt/lists/*

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]