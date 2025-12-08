from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
import time

from app.database import Base, engine
from app.routers import items


def wait_for_db(retries=10, delay=3):
    """Retry database connection until MySQL is ready."""
    for i in range(retries):
        try:
            Base.metadata.create_all(bind=engine)
            print("Database connected and tables created!")
            return
        except OperationalError:
            print(
                f"Database connection failed ({i + 1}/{retries}). "
                f"Retrying in {delay}s..."
            )
            time.sleep(delay)

    raise Exception(
        "Could not connect to the database after multiple retries."
    )


# Initialize FastAPI app
app = FastAPI(title="FastAPI MySQL Docker App")

# Include routers
app.include_router(items.router)


@app.get("/")
def home():
    return {
        "message": "FastAPI + MySQL + SQLAlchemy + Docker working!"
    }


# NOTE: This block prevents wait_for_db() from running during pytest
if __name__ == "__main__":
    wait_for_db()
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
