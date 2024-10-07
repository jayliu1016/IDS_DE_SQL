# BooksDB Application

## Overview
This Python application connects to a SQLite database and performs basic CRUD operations on a books table. The application includes CI/CD with GitHub Actions.

## Setup

1. Clone the repository.
2. Build the Docker image: `make docker-build`
3. Run the application in Docker: `make docker-run`

## Requirements
- Python 3.10
- Docker (optional)
- sqlite3
- pytest

## Testing
Run the tests with:
```bash
make test
