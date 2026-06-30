# fastapi_dispatch_mangement
This project is develop to learn FastAPI and also can be used to logistic dispatch management.

# FastAPI Project

A FastAPI-based REST API application.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.10 or above
- pip
- Git
- Virtual Environment (recommended)

Verify your Python version:

```bash
python --version
```

---

## Clone the Repository

```bash
git clone <repository_url>
cd <project_directory>
```

---

## Create a Virtual Environment

### Linux/macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```cmd
python -m venv venv
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

If using Poetry:

```bash
poetry install
```

---

## Configure Environment Variables

Create a `.env` file in the project root.

Example:

```env
APP_NAME=FastAPI Project
HOST=0.0.0.0
PORT=8000
DEBUG=True

DATABASE_URL=postgresql://username:password@localhost:5432/database_name

SECRET_KEY=your_secret_key

JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

Update the values according to your environment.

---

## Database Migration (Alembic)

Run the latest migrations:

```bash
alembic upgrade head
```

Create a new migration:

```bash
alembic revision --autogenerate -m "Migration message"
```

---

## Run the Application

### Development Mode

```bash
uvicorn app.main:app --reload
```

or

```bash
python -m uvicorn app.main:app --reload
```

If your application entry point is different, update the command accordingly.

Example:

```bash
uvicorn main:app --reload
```

---

## API Documentation

Once the application starts, visit:

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

OpenAPI JSON

```
http://localhost:8000/openapi.json
```

---

## Running Tests

Using pytest:

```bash
pytest
```

Generate coverage report:

```bash
pytest --cov=app
```

---

## Project Structure

```
project/
│
├── app/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   ├── dependencies.py
│   └── main.py
│
├── alembic/
├── tests/
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Common Commands

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
uvicorn app.main:app --reload
```

Run tests:

```bash
pytest
```

Format code:

```bash
black .
```

Sort imports:

```bash
isort .
```

Lint:

```bash
flake8
```

---

## Troubleshooting

### ModuleNotFoundError

Ensure the virtual environment is activated and dependencies are installed.

### Port Already in Use

Run on another port:

```bash
uvicorn app.main:app --reload --port 8001
```

### Database Connection Error

- Verify `.env` values.
- Ensure the database is running.
- Confirm database credentials.

### Migration Issues

Check the current migration version:

```bash
alembic current
```

Upgrade to the latest migration:

```bash
alembic upgrade head
```

---

## Stopping the Server

Press:

```
CTRL + C
```

---
