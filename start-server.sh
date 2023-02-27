#!/bin/bash

# Build the Docker image
docker build --tag flamapyapi .

# Run the Docker image
docker run --name flamapy.api -it -p 5000:5000 flamapyapi

# Stop the Docker container
docker stop flamapy.api

# Remove the Docker container
docker rm flamapy.api

# Remove the Docker image
docker rmi flamapyapi