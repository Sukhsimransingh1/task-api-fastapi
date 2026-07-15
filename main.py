from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="Simple CRUD API using FastAPI",
    version="1.0"
)

# Request Model
class TaskCreate(BaseModel):
    title: str


# In-memory Database
tasks = [
    {
        "id": 1,
        "title": "Learn FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "Complete FlyRank Assignment",
        "done": False
    },
    {
        "id": 3,
        "title": "Practice Python",
        "done": True
    }
]


# Root Endpoint
@app.get("/", summary="API Information")
def root():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }


# Health Check
@app.get("/health", summary="Health Check")
def health():
    return {
        "status": "ok"
    }


# Get All Tasks
@app.get("/tasks", summary="Get All Tasks")
def get_tasks():
    return tasks


# Get Task By ID
@app.get("/tasks/{task_id}", summary="Get Task By ID")
def get_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# Create New Task
@app.post(
    "/tasks",
    summary="Create New Task",
    status_code=status.HTTP_201_CREATED
)
def create_task(task: TaskCreate):

    title = task.title.strip()

    if title == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "done": False
    }

    tasks.append(new_task)

    return new_task