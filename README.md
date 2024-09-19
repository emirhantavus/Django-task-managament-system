# 📝 Task Management System

This project is a Task Management System developed using Django Rest Framework (DRF). It allows users to create projects, add tasks, and assign these tasks to specific users. Role-based access controls enable managing user permissions effectively.

## 🚀 Project Features

- **Create, list, and update projects and tasks:** Users can manage projects and related tasks with ease.
- **Role-based authorization:** Two roles are defined: Project Manager and Developer. Project Managers can create and manage tasks and projects, while Developers can only update and view tasks.
- **Assign tasks to multiple users:** Tasks can be assigned to multiple users for collaborative work.
- **Scheduled tasks using Celery and Redis:** Tasks can be scheduled for specific times, and notifications can be sent before deadlines.

## 📦 Technologies Used

- **Django 5.0.1** - Web framework used for developing the backend.
- **Django Rest Framework (DRF)** - For building and consuming RESTful APIs.
- **PostgreSQL** - Database for storing user, project, and task data.
- **Redis** - In-memory data structure store used for background tasks and queue management.
- **Celery** - Asynchronous task management and scheduling.
- **Postman** - For API testing and documentation.
- **Git and GitHub** - Version control and code repository.

## 📚 Development Approaches

### ✅ Test-Driven Development (TDD)
Test-Driven Development (TDD) was implemented to ensure code quality and reliability.

- **Test Cases Include:**
  - Testing user and role creation.
  - Testing project and task creation with validation checks.
  - Testing API endpoints for authorized and unauthorized access.

### 🌐 Domain-Driven Design (DDD)
Domain-Driven Design (DDD) principles were used to create a clear separation between the business logic and technical concerns.

- **Domain Models:**
  - `User`: Custom user model with roles.
  - `Project`: Represents a project entity with relationships to tasks and users.
  - `Task`: Represents a task entity with relationships to users and projects.

## 📄 API Endpoints

### Project Endpoints

1. **List all projects:**
   - **Endpoint:** `GET /api/projects/`
   - **Description:** Returns a list of all projects.
   - **Response:**
   ```json
   [
       {
           "id": 1,
           "name": "Project 1",
           "description": "This is project 1",
           "created_at": "2023-09-19T12:00:00Z",
           "updated_at": "2023-09-19T12:00:00Z"
       }
   ]

2. **Create new project:**
   - **Endpoint:** `POST /api/projects/`
   - **Description:** Create a project.
   - **Body:**
    ``` json
   [
       {
           "name": "Project 1",
           "description": "This is project 1",
       }
   ]
3. **Retrieve a specific project:**
   - **Endpoint:** `GET /api/projects/1/`
   - **Description:** Returns a specific project by ID.
   - **Response:**
    ``` json
   [
       {
           "id" : 1,
           "name": "Project 1",
           "description": "This is project 1",
           "created_at": "2024-09-19T12:00:00Z",
           "updated_at": "2024-09-19T12:00:00Z"
       }
   ]

### Task Endpoints
1. **List all tasks**
   - **Endpoint:** - `GET /api/tasks/`
2. **Create tasks**
   - **Endpoint:** - `POST /api/tasks`
3. **Update task completed**
   - **Endpoint:** - `PATCH /api/tasks/1/`
   - **Headers:** - `Authorization: Bearer <your_token>`
   - **Body:**
     ``` json
     [
       {
         "is_completed":true
       }
     ]
  - **Response:**
    ``` json
    [
      {
      "id": 1,
      "title": "Task 1",
      "description": "This is task 1",
      "is_completed": true,
      "project": 1,
      "users": ["emirhantavus17@gmail.com"],
      "created_at": "2024-09-19T12:00:00Z",
      "updated_at": "2024-09-19T14:00:00Z"
      }
    ]

4. **Delete task**
   - **Endpoint** - `DELETE /api/tasks/{id}/`
