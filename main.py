from fastapi import FastAPI
from pydantic import BaseModel

# Create an instance of FastAPI
app = FastAPI(title="Simple API", description="A simple API to demonstrate Swagger", version="1.0.0")

# Data model for a user
class User(BaseModel):
    id: int
    name: str
    email: str

# In-memory database (list of users)
users = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the Simple API"}

@app.get("/users", summary="Get all users", description="Fetches all users in the system.")
def get_users():
    return {"users": users}

@app.post("/users", summary="Create a user", description="Adds a new user to the system.")
def create_user(user: User):
    users.append(user.dict())
    return {"message": "User created successfully", "user": user}

@app.get("/users/{user_id}", summary="Get user by ID", description="Fetches a user by their ID.")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"error": "User not found"}

@app.delete("/users/{user_id}", summary="Delete a user", description="Deletes a user by their ID.")
def delete_user(user_id: int):
    global users
    users = [user for user in users if user["id"] != user_id]
    return {"message": "User deleted successfully"}
