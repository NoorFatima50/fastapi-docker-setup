#!/bin/bash
set -e

# Variables
APP_NAME="fastapi-app"
DOCKER_IMAGE="your_dockerhub_username/$APP_NAME:latest"

# Functions
build_image() {
    echo "Building Docker image..."
    docker build -t $DOCKER_IMAGE ..
}

push_image() {
    echo "Pushing Docker image..."
    docker push $DOCKER_IMAGE
}

# Main script
echo "Starting script..."
build_image
push_image
echo "Script completed successfully!"
