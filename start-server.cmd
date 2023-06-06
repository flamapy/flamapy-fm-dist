@echo OFF

REM Build the Docker image
docker build --tag flamapyapi .

REM Run the Docker image
docker run --name flamapy.api -it -p 8000:8000 flamapyapi

REM Stop the Docker container
docker stop flamapy.api

REM Remove the Docker container
docker rm flamapy.api

REM Remove the Docker image
docker rmi flamapyapi