
# Python Application Dockerization

## Overview

This project demonstrates how to containerize a Python application using Docker.

The Dockerfile uses Ubuntu as the base image, installs Python 3 and pip, copies the application files into the container, configures environment variables, and executes the Python application using the CMD instruction.

## Technologies Used

- Docker
- Ubuntu
- Python 3
- pip
- Dockerfile

## Dockerfile Explanation

### 1. Base Image
```dockerfile
FROM ubuntu:latest
```
Uses the latest Ubuntu image as the base image.

### 2. Set Working Directory
```dockerfile
WORKDIR /app
```
Creates and sets `/app` as the working directory inside the container.

### 3. Copy Application Files
```dockerfile
COPY . /app
```
Copies all files from the current host directory into the container's `/app` directory.

### 4. Install Python
```dockerfile
RUN apt-get update && apt-get install -y python3 python3-pip
```
Updates Ubuntu package repositories and installs Python 3 and pip.

### 5. Configure Environment Variable
```dockerfile
ENV NAME World
```
Defines an environment variable named `NAME` with the value `World`.

### 6. Start the Application
```dockerfile
CMD ["python3", "app.py"]
```
Executes the Python application when the Docker container starts.

## Project Workflow

1. Pull the Ubuntu base image.
2. Create the application working directory.
3. Copy application files into the image.
4. Install Python 3 and pip.
5. Configure environment variables.
6. Execute `app.py` inside the container.

## How to Run the Project

### Clone the Repository
```bash
git clone <your-repository-url>
cd <repository-name>
```

### Build Docker Image
```bash
docker build -t python-docker-app .
```

### Run Docker Container
```bash
docker run --name python-app-container python-docker-app
```

### Run with a Custom Environment Variable
```bash
docker run -e NAME=Surya python-docker-app
```

### View Containers
```bash
docker ps -a
```

### Remove Container
```bash
docker rm python-app-container
```

### Remove Docker Image
```bash
docker rmi python-docker-app
```

## Key Learning Outcomes

- Understanding Dockerfile instructions.
- Containerizing Python applications.
- Installing application dependencies inside Docker.
- Using Docker environment variables.
- Understanding the difference between RUN and CMD.
- Building Docker images and running containers.

```
