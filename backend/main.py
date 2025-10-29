from typing import Union
from fastapi import FastAPI
import psycopg2
from psycopg2 import OperationalError
import os

app = FastAPI()

# Database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST", "postgres-service"),  # Kubernetes service name
    "port": os.getenv("DB_PORT", "5432"),
    "database": os.getenv("DB_NAME", "trainingdb"),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "password")
}

def test_db_connection():
    """Test database connection and return True/False"""
    try:
        # Attempt to connect
        conn = psycopg2.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            database=DB_CONFIG["database"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            connect_timeout=5  # 5 second timeout
        )
        
        # Test with a simple query
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()
        conn.close()
        
        return True
    except OperationalError as e:
        print(f"Database connection failed: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health/db")
def check_db():
    """Check database connection health"""
    is_connected = test_db_connection()
    
    return {
        "database_connected": is_connected,
        "database_host": DB_CONFIG["host"],
        "database_name": DB_CONFIG["database"],
        "status": "healthy" if is_connected else "unhealthy"
    }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}