import os

DB_USER = os.getenv("POSTGRES_USER", "fastapi_user")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "fastapi_pass")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("POSTGRES_DB", "car_moto_store")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"