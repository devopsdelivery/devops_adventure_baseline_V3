from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import psycopg2
from psycopg2.extras import RealDictCursor
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Database connection settings
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "adventure_db"
DB_USER = "postgres"
DB_PASSWORD = "123"  # Replace with your actual password

# Create a database connection
def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

class User(BaseModel):
    name: str
    email: str

# Endpoint to get all users
@app.get("/users", response_model=List[User])
async def read_users():
    conn = get_db_connection()
    with conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT ID, Name, Email FROM Users;")
            users = cursor.fetchall()
    return users

# Endpoint to create a new user
@app.post("/users", response_model=User)
async def create_user(user: User):
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO Users (Name, Email) VALUES (%s, %s) RETURNING ID;",
                (user.name, user.email)
            )
            user_id = cursor.fetchone()[0]
            conn.commit()
    return {**user.dict(), "id": user_id}

# Endpoint to delete a user by ID
@app.delete("/users/{user_id}", response_model=User)
async def delete_user(user_id: int):
    conn = get_db_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Users WHERE ID = %s;", (user_id,))
            user = cursor.fetchone()
            if user is None:
                raise HTTPException(status_code=404, detail="User not found")
            
            cursor.execute("DELETE FROM Users WHERE ID = %s;", (user_id,))
            conn.commit()
    return {"id": user[0], "name": user[1], "email": user[2]}

