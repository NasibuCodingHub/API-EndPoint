# API-EndPoint
## Students and Subjects API

A Flask-based REST API for managing student records and course subjects.

## 📌 Table of Contents
1.Branches <br>
2.Branches <br>
3.Setup <br>
4.Endpoints <br>
5.Running the App <br>
6.Git Workflow <br>


## ✨ Branches
✅ Students Endpoint – Retrieve student data (name, program).<br>
✅ Subjects Endpoint – Fetch course subjects grouped by year and status (Core/Elective).<br>
✅ MySQL Integration – Uses pymysql for database operations.<br>
✅ Branch-Based Development – Endpoints developed in separate Git branches (students-endpoint, subjects-endpoint).<br>


## 🌿 Branches
| Branch             | Description               | File           |
|--------------------|---------------------------|---------------|
| `main`            | Merged final version       | `app.py`      |
| `students-endpoint` | Only `/students` endpoint | `students_app.py` |
| `subjects-endpoint` | Only `/subjects` endpoint | `subjects_app.py` |

## API Endpoints
### Students API (`students-endpoint` Branch)
- **Endpoint:** `GET /students`
- **Response:** JSON list of students with name and program.

### Subjects API (`subjects-endpoint` Branch)
- **Endpoint:** `GET /subjects`
- **Response:** JSON list of subjects grouped by year and status.

## ⚙️ Setup

Prerequisites

# Python 3.8+

Flask (pip install flask)

PyMySQL (pip install pymysql)

MySQL (XAMPP recommended)

# Database Setup

Create a database students_db in MySQL.

Import the provided students_db.sql file to set up tables and sample data.

## 🔌 Endpoints
# 1. /students
📝 Description: Fetches all student records.<br>
🔹 Method: GET <br>
📂 Response:<br>

# 2. /subjects
📝 Description: Fetches subjects grouped by year and status.<br>
🔹 Method: GET <br>
📂 Response: <br>
