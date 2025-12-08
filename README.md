🔹FastAPI Application
Built a modular FastAPI backend with separate files for models, database configuration, schemas, and API routers.
Implemented REST API endpoints to create and retrieve items.
Automatic interactive API documentation available via Swagger UI (/docs).

🔹MySQL Database Integration
Used SQLAlchemy ORM to manage MySQL database operations.
MySQL runs inside a Docker container using docker-compose.yml.
Tables are automatically created using Base.metadata.create_all(bind=engine).

🔹 Docker & Containerization
Entire project is fully containerized using Docker.
docker-compose launches both FastAPI and MySQL services.
Ensures consistent environment across all systems.
Allows easy deployment with a single command:
        docker compose up -d

🔹 CI/CD with GitHub Actions
Implemented GitHub Actions workflow for automation.
CI pipeline runs on every push to main and includes:
Code checkout
Docker Compose service startup
Linting with flake8
Running tests using Pytest
Building Docker image
Pushing image to Docker Hub automatically
Ensures clean code and prevents broken updates.

🔹 Testing Setup (Pytest)
Added automated tests for API endpoints and schema validation.
Tests verify item creation, retrieval, and correct JSON structure.
Helps catch issues early and maintain high code reliability.

🔹 Docker Hub Integration
Configured workflow to log in to Docker Hub using GitHub secrets.
Automatically builds and pushes the latest image:
    noorfatima21/fastapi-app
