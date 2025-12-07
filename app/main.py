from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
import time

from app.database import Base, engine
from app.routers import items


# Retry function to wait for DB to be ready
def wait_for_db(retries=10, delay=3):
    for i in range(retries):
        try:
            # Try connecting to DB and creating tables
            Base.metadata.create_all(bind=engine)
            print("Database connected and tables created!")
            return
        except OperationalError:
            print(
                f"Database connection failed ({i+1}/{retries}). "
                f"Retrying in {delay}s..."
            )
            time.sleep(delay)

    raise Exception(
        "Could not connect to the database "
        "after multiple retries."
    )


# Initialize FastAPI app
app = FastAPI(title="FastAPI MySQL Docker App")

# Include the items router
app.include_router(items.router)

# Wait for DB before starting
wait_for_db()


# Optional: simple root endpoint
@app.get("/")
def home():
    return {
        "message": "FastAPI + MySQL + SQLAlchemy + Docker working!"}
