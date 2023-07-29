# Python API Proof of Concept

[![Build Status](https://github.com/atxpaul/API-Rest-Python-PoC/actions/workflows/ci.yml/badge.svg)](https://github.com/atxpaul/API-Rest-Python-PoC/actions/workflows/ci.yml)

This repository contains a simple Proof of Concept (PoC) for a Python API that returns the current time.


## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Docker Image](#docker-image)
- [Contributing](#contributing)

## Introduction

This PoC demonstrates the implementation of a simple Python API using Flask to return the current time. It includes a basic directory structure, a set of API endpoints, and tests to ensure the functionality is correct.

## Features

- Get the current time from the API.
- Organized directory structure following the production-grade pattern.
- Unit tests for the API endpoints and services.
- Dockerfile for containerization.

## Getting Started

### Prerequisites

Make sure you have the following software installed:

- Python (version 3.9 recommended)
- Docker (if you want to build the Docker image)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/<YOUR_USERNAME>/<YOUR_REPOSITORY>.git
cd <YOUR_REPOSITORY>
```

2. Set up a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\Activate.ps1
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Running the application

To start the API server, run the following command:

```bash
python main.py
```

The API will be accessible at http://localhost:5000/time.

### API Endpoints

The API provides the following endpoint:

- GET /time: Returns the current time as a JSON response.

### Running Tests

To run the tests, use the following command:

```bash
python -m unittest discover -s tests
```

### Docker Image

The repository is configured with a GitHub Actions workflow that automatically builds and pushes a Docker image to Docker Hub when you push changes to the main branch.

The Docker image can also be built locally using the provided Dockerfile:

```bash
docker build -t atxpaul/python_api_poc:latest .
```

### Contributing

Contributions to this PoC are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.