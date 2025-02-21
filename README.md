# Task App Management

## Prerequisites
- Python 3.13.x
- PostgreSQL 17.x (run via docker-compose file)

## How to run the API

### Environment variables

- `DB_URL=<postgres-url>`

### From source code

1. Run the database via the `docker compose up -d` command
2. Create a Python virtual environment to install the required dependencies to run the REST API, for instance: `python -m venv .venv`
3. Install the required dependencies with `pip install -r requirements.txt` command
4. Once the dependencies are installed and that you have the database up and running you can run the application
    - 4.1. Either in development mode from the root folder: `fastapi dev main.py`
    - 4.2. Or in production mode: `fastapi run main.py`

## How to run tests

### Environment variables

To run the tests it is mandatory to create a .env.test file with the environment variables listed on the __How to run the API section__

### Steps

1. Run the database via the `docker compose up -d` command
2. Create a Python virtual environment to install the required dependencies to run the REST API, for instance: `python -m venv .venv`
3. Install the required dependencies with `pip install -r requirements.txt` command
4. Once the dependencies are installed and that you have the database up and running you can run the tests with the command: `pytest`