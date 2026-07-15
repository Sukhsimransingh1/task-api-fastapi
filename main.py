from fastapi import FastAPI, HTTPException, status
from fastapi.responses import Response
from pydantic import BaseModel
from typing import Optional

app = FastAPI(
    title="Task API",
    description="Simple CRUD API using FastAPI",
    version="1.0"
)

# Request Models
class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None


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
    return {"status": "ok"}


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


# Create Task
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

    next_id = max(task["id"] for task in tasks) + 1 if tasks else 1

    new_task = {
        "id": next_id,
        "title": title,
        "done": False
    }

    tasks.append(new_task)

    return new_task


# Update Task
@app.put("/tasks/{task_id}", summary="Update Task")
def update_task(task_id: int, updated_task: TaskUpdate):

    for task in tasks:

        if task["id"] == task_id:

            if updated_task.title is not None:

                if updated_task.title.strip() == "":
                    raise HTTPException(
                        status_code=400,
                        detail="Title cannot be empty"
                    )

                task["title"] = updated_task.title.strip()

            if updated_task.done is not None:
                task["done"] = updated_task.done

            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )


# Delete Task
@app.delete(
    "/tasks/{task_id}",
    summary="Delete Task",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_task(task_id: int):

    for index, task in enumerate(tasks):

        if task["id"] == task_id:
            tasks.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )