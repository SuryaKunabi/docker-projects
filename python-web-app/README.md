# Python Web App with Docker

## Overview

This project demonstrates how to **containerize a Python web application using Docker**.

Instead of installing Python and the application's dependencies directly on the host machine, Docker packages the application and its dependencies into a container.

```text
Python Web Application
        ↓
    Dockerfile
        ↓
    Docker Image
        ↓
   Docker Container
        ↓
 Running Web Application
```

---

## Technologies Used

* Python
* Python Web Framework
* Docker
* Dockerfile
* Docker Container

---

## Project Structure

```text
python-web-app/
│
├── Dockerfile
├── requirements.txt
├── app.py
└── ...
```

> The exact file names may vary depending on the application structure.

### Dockerfile

Contains the instructions required to build the Docker image.

### requirements.txt

Contains the Python dependencies required by the application.

### app.py

Contains the main Python web application.

---

# Docker Concepts Demonstrated

This project demonstrates the basic Docker workflow:

```text
Application Code
       ↓
Dockerfile
       ↓
docker build
       ↓
Docker Image
       ↓
docker run
       ↓
Docker Container
       ↓
Web Application
```

---

# Prerequisites

Before running the project, install:

* Docker Desktop
* Git

Verify Docker:

```bash
docker --version
```

Verify Docker Compose if required:

```bash
docker compose version
```

---

# Run the Application

## 1. Clone the Repository

```bash
git clone https://github.com/SuryaKunabi/docker-projects.git
```

Move into the project:

```bash
cd docker-projects/python-web-app
```

---

## 2. Build the Docker Image

Run:

```bash
docker build -t python-web-app .
```

Explanation:

```text
docker build
    ↓
Reads Dockerfile
    ↓
Installs dependencies
    ↓
Copies application files
    ↓
Creates Docker Image
```

Check the image:

```bash
docker images
```

---

## 3. Run the Container

Run the application:

```bash
docker run -d -p 8000:8000 --name python-web-app python-web-app
```

The exact port may need to match the port configured by the application.

---

## 4. Check the Container

```bash
docker ps
```

You should see the running container:

```text
CONTAINER ID
IMAGE
STATUS
PORTS
NAMES
```

---

## 5. Access the Application

Open a browser and visit:

```text
http://localhost:8000
```

If the application uses another port, replace `5000` with the configured port.

---

# View Container Logs

To see application output:

```bash
docker logs python-web-app
```

For live logs:

```bash
docker logs -f python-web-app
```

Press:

```text
Ctrl + C
```

to stop following the logs.

---

# Stop the Container

```bash
docker stop python-web-app
```

---

# Start the Container Again

```bash
docker start python-web-app
```

---

# Remove the Container

```bash
docker rm python-web-app
```

If the container is still running:

```bash
docker rm -f python-web-app
```

---

# Remove the Docker Image

```bash
docker rmi python-web-app
```

---

# Why Containerize a Python Application?

Without Docker, the application requires the correct Python version and dependencies to be installed on the host machine.

With Docker:

```text
Python
   +
Dependencies
   +
Application
   ↓
Docker Image
   ↓
Container
```

This makes the application environment more consistent and easier to reproduce across development, testing, and deployment environments.

---

