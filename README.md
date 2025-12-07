FastAPI Docker Setup
A simple FastAPI project using MySQL, Docker, and GitHub Actions for CI/CD. This project includes basic CRUD operations, database setup, environment configuration, and automation scripts.

Features
FastAPI backend with a sample items route
MySQL database using Docker
.env file for configuration
Dockerfile + Docker Compose setup
CI/CD with GitHub Actions
Bash scripts for build & run automation

How to Run
1. Create .env file
Copy the example file:
cp .env.example .env
2. Start the app with Docker
docker-compose up --build
API will be available at: http://localhost:8000/docs

CI/CD
GitHub Actions workflow runs on every push to check Docker build and run basic tests.

Bash Scripts
scripts/build.sh → Builds Docker image
scripts/run.sh → Runs app container
