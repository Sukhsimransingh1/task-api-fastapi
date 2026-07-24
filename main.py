from fastapi import FastAPI
import sqlite3

app = FastAPI(
    title="Task API",
    description="SQLite CRUD API",
    version="2.0"
)

DATABASE = "tasks.db"


# Database Initialization
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL
        )
    """)

    # Check if table is empty
    cursor.execute("SELECT COUNT(*) FROM tasks")
    count = cursor.fetchone()[0]

    # Seed data only once
    if count == 0:
        cursor.executemany(
            "INSERT INTO tasks (title, done) VALUES (?, ?)",
            [
                ("Learn FastAPI", 0),
                ("Complete FlyRank Assignment", 0),
                ("Practice Python", 1)
            ]
        )

    conn.commit()
    conn.close()


# Initialize database
init_db()


# Existing Endpoints
@app.get("/")
def root():
    return {
        "name": "Task API",
        "version": "2.0",
        "endpoints": [
            "/tasks"
        ]
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }