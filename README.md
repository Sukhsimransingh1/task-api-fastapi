# 🚀 Task API

A simple RESTful CRUD API built using **FastAPI** for managing tasks.

## 🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## ⚙️ Installation

```bash
git clone https://github.com/Sukhsimransingh1/flyrank-task-api.git
cd flyrank-task-api

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt
```

## ▶️ Run the Project

```bash
uvicorn main:app --reload
```

Open your browser:

- **API:** http://127.0.0.1:8000
- **Swagger UI:** http://127.0.0.1:8000/docs

---

## 📌 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | API Information |
| GET | `/health` | Health Check |
| GET | `/tasks` | Get All Tasks |
| GET | `/tasks/{task_id}` | Get Task By ID |
| POST | `/tasks` | Create New Task |
| PUT | `/tasks/{task_id}` | Update Task |
| DELETE | `/tasks/{task_id}` | Delete Task |

---

## 🧪 Example cURL

```bash
curl -i -X POST http://127.0.0.1:8000/tasks \
-H "Content-Type: application/json" \
-d "{\"title\":\"Buy Milk\"}"
```

---

## 📷 Swagger UI

![Swagger UI](images/swagger-ui.png)

---

## 👨‍💻 Author

**Sukhsimran Singh**

GitHub: https://github.com/Sukhsimransingh1