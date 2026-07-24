# FlyRank Task API (SQLite)

A RESTful Task Management API built with **FastAPI** and **SQLite**. The API supports full CRUD (Create, Read, Update, Delete) operations with persistent data storage.

---

## Features

- Create a task
- Get all tasks
- Get a task by ID
- Update a task
- Delete a task
- SQLite database for persistent storage
- Interactive Swagger UI documentation

---

## Tech Stack

- Python 3
- FastAPI
- SQLite
- Pydantic
- Uvicorn

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sukhsimransingh1/flyrank-task-api.git
cd flyrank-task-api
```

Create a virtual environment:

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Root endpoint |
| GET | `/health` | Health check |
| GET | `/tasks` | Get all tasks |
| GET | `/tasks/{id}` | Get task by ID |
| POST | `/tasks` | Create a new task |
| PUT | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

---

## SQLite Database

The application uses SQLite for persistent storage. The database (`tasks.db`) and the `tasks` table are created automatically when the application starts. Three sample tasks are inserted only if the table is empty.

Example SQL query:

```sql
SELECT * FROM tasks;
```

---

## Screenshots

### Swagger UI

![Swagger UI](images/swagger-ui.png)

### SQLite Database

![SQLite Database](images/sqlite-db.png)

---

## Project Structure

```
flyrank-task-api/
│── images/
│   ├── swagger-ui.png
│   └── sqlite-db.png
│── main.py
│── README.md
│── requirements.txt
│── .gitignore
```

---

## Author

**Sukhsimran Singh**