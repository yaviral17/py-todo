# FastAPI Todo App with PostgreSQL

This repository contains a robust **Todo API** built using **FastAPI** and connected to a **PostgreSQL** database. The application provides full CRUD (Create, Read, Update, Delete) functionality for managing todo items, with the database running inside a Docker container and using SQLAlchemy for ORM.

## Table of Contents
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Set Up Docker](#2-set-up-docker)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Create the PostgreSQL Database](#4-create-the-postgresql-database)
  - [5. Run the FastAPI Application](#5-run-the-fastapi-application)
- [API Endpoints](#api-endpoints)
- [Database Operations](#database-operations)
- [Error Handling](#error-handling)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [License](#license)

## Features

- **CRUD** functionality for Todo items:
  - Create new todos
  - Retrieve all todos or a specific todo by ID
  - Update existing todos
  - Delete todos
- **PostgreSQL** database for persistent storage
- **SQLAlchemy** ORM for database interactions
- **Docker** for containerized development
- **FastAPI** for creating a robust and fast API with automatic documentation
- **Pydantic** models for request validation and response serialization
- Secure database operations with parameterized queries
- Comprehensive error handling and logging

## Project Structure

The project is structured as follows:

1. **FastAPI Application**: The main application setup using FastAPI.
2. **Database Configuration**: SQLAlchemy configuration for PostgreSQL connection.
3. **Models**: 
   - SQLAlchemy `Task` model representing todo items in the database.
   - Pydantic models for request/response handling.
4. **API Endpoints**: Implementation of CRUD operations.
5. **Database Operations**: Functions for secure database interactions.
6. **Error Handling**: Custom error handling and logging.

## Requirements

- Docker & Docker Compose
- Python 3.7+
- PostgreSQL
- FastAPI
- SQLAlchemy
- Pydantic

## Setup Instructions

### 1. Clone the Repository

Start by cloning this repository to your local machine:

```bash
https://github.com/Mr-CodeBin/py-todo.git
cd py-todo
```

### 2. Set Up Docker

This app uses Docker to run PostgreSQL. Make sure you have Docker installed on your system. The `docker-compose.yml` file is included to easily set up the database.

Run the following command to build the Docker containers:

```bash
docker-compose up -d
```

This will set up the **PostgreSQL** container.

### 3. Install Dependencies

After setting up Docker, create a virtual environment and install the necessary dependencies for the FastAPI app:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # For Linux/MacOS
# or
venv\Scripts\activate  # For Windows

# Install the dependencies
pip install -r requirements.txt
```

### 4. Create the PostgreSQL Database

Before starting the app, you need to create the PostgreSQL database. The connection details are already set in the configuration file.

- Database Name: `todo`
- Username: `root`
- Password: `test1234`
- Host: `localhost`
- Port: `6789`

You can create the database manually inside the PostgreSQL container, or use any database client like `pgAdmin`.

```sql
CREATE DATABASE todo;
```

### 5. Run the FastAPI Application

Once the database is set up, you can run the FastAPI application:

```bash
uvicorn main:app --reload
```

The API will now be available at `http://127.0.0.1:8000`.

## API Endpoints

The following CRUD endpoints are implemented:

- `GET /`: A simple welcome message.
- `GET /todos`: Retrieve a list of all todos.
- `GET /todos/{todo_id}`: Retrieve a specific todo by its ID.
- `POST /todos`: Create a new todo.
  - Body example:
    ```json
    {
      "title": "New Task",
      "description": "This is a new task",
      "due_date": "2022-12-12",
      "priority": "high",
      "completed": false
    }
    ```
- `PUT /todos/{todo_id}`: Update a todo by its ID.
  - Body example:
    ```json
    {
      "title": "Updated Task",
      "description": "Updated task description",
      "due_date": "2022-12-12",
      "priority": "low",
      "completed": true
    }
    ```
- `DELETE /todos/{todo_id}`: Delete a todo by its ID.

## Database Operations

- Database operations are handled using SQLAlchemy ORM.
- Parameterized queries are used to prevent SQL injection.
- Proper exception handling and transaction management are implemented.
- Database connections and cursors are properly closed after operations.

## Error Handling

- Comprehensive error handling is implemented to catch and log exceptions.
- Meaningful error messages and appropriate HTTP status codes are returned to the client.
- Custom error handling ensures a robust user experience.

## Running Tests

You can run tests by executing the following command:

```bash
pytest
```

Ensure you have `pytest` installed:

```bash
pip install pytest
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
