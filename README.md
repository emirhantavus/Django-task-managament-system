### 📝Task Management System

This project is a Task Management System developed using Django Rest Framework (DRF). Users can create projects, add tasks, and assign these tasks to specific users. Role-based access controls allow managing user permissions.

# 🚀 Project Features

Create, list, and update projects and tasks.
Role-based authorization (Project Manager and Developer roles).
Assigning tasks to multiple users.
Scheduled tasks using Celery and Redis.
Advanced error management with user-friendly error messages.

# 📦 Technologies Used 

Django 5.0.1
Django Rest Framework (DRF)
PostgreSQL - Database
Redis - For background tasks and queue management
Celery - Asynchronous task management
Postman - For API testing
Git and GitHub - Version control system

# 📄 API Endpoints 

** Project Endpoints **
GET /api/projects/ - List all projects.
POST /api/projects/ - Create a new project.
GET /api/projects/{id}/ - Retrieve a specific project.

** Task Endpoints **
GET /api/tasks/ - List all tasks.
POST /api/tasks/ - Create a new task.
PATCH /api/tasks/{id}/ - Update a specific task.
DELETE /api/tasks/{id}/ - Delete a specific task.