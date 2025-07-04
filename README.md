# SDF Student Manager
I developed this web application to simplify student grading and presence management for a "Software Development Fundamentals" course. It was later also used as an example webpp for the course.

![image](https://github.com/user-attachments/assets/d12ea394-8152-4000-99b4-dde9dd076b18)

## Features
This application provides comprehensive functionalities for managing students, groups, and lessons, including:

**- Student Management**:

  - Register new students.

  - View student details, including grades and presence.

  - Edit existing student information.

  - Delete student records.

  - Manage student grades.

**- Group Management**:

  - Register new groups.

  - View group details, including members, tracking links, and repository links.

  - Edit existing group information.

  - Delete groups.

**- Lesson Management**:

  - Add new lessons with roll call functionality.

  - View and manage all lessons.

  - Edit lesson details, including student presence.

  - Delete lessons.

# Technologies Used
The project is built using the following technologies:

**- Django**: A high-level Python Web framework.

**- Python**: The primary programming language (version 3.11 specified).

**- Bootstrap**: Used for styling the web application.

**- jQuery**: A JavaScript library for DOM manipulation and event handling.

**- SQLite**: Database used for local development.

**- PostgreSQL**: Database used for production environments.

**- Gunicorn**: A Python WSGI HTTP Server for UNIX.

**- Whitenoise**: For serving static files in production.

**- python-dotenv**: For managing environment variables.

**- uv**: A fast Python package installer and resolver.

## Setup and Installation
To set up the project locally, follow these steps:

**1. Ensure Python 3.13 and uv are installed on your system**.

**2. Clone the repository**:
  ```bash
  git clone https://github.com/jvitorcarv/sdf-student-manager.git
  cd sdf-student-manager/student_presence
  ```

**3. Create and activate a virtual environmente using `uv`**:
  ```bash
  uv venv
  source .venv/bin/activate  # On macOS/Linux
  # or
  .venv\Scripts\activate # On Windows
  ```

**4. Install dependencies**:
  ```bash
  uv init
  uv sync
  ```

**5. Apply database migrations**:
```bash
python manage.py makemigrations presence_count
python manage.py migrate
```


**6. Create a Superuser (optional, for admin access)**:
```bash
python manage.py createsuperuser
```

## Usage
Run the development server:
```bash
python manage.py runserver
```

Open your web browser and navigate to http://127.0.0.1:8000/.

Use the navigation bar to access different sections like Student, Group, and Lesson management.

## Project Structure
The core application logic resides in the student_presence directory, with presence_count being the main Django app:

```
sdf-student-manager/
├── .github/
│   └── workflows/
│       └── main_sdf-student-manager.yml  (Azure Web App deployment)
└── student_presence/
    ├── manage.py                       (Django management utility)
    ├── presence_count/
    │   ├── admin.py                    (Admin site configurations)
    │   ├── apps.py                     (App configuration)
    │   ├── forms.py                    (Django forms)
    │   ├── models.py                   (Database models for Student, Group, Lesson)
    │   ├── static/                     (Static files: CSS, JS)
    │   │   ├── css/
    │   │   └── js/
    │   ├── templates/                  (HTML templates for various views)
    │   │   ├── group/
    │   │   ├── imgs/
    │   │   ├── lesson/
    │   │   ├── menus/
    │   │   ├── snippets/
    │   │   └── student/
    │   ├── tests.py                    (Application tests)
    │   ├── urls.py                     (URL routing for the app)
    │   └── views.py                    (View functions)
    ├── pyproject.toml                  (Python dependencies)
    ├── uv.lock                         (Python dependencies)
    └── student_presence/               (Main Django project settings)
        ├── asgi.py
        ├── settings.py                 (Project settings)
        ├── urls.py                     (Project-level URL configurations)
        └── wsgi.py
```

## Deployment
The repository includes a GitHub Actions workflow (`.github/workflows/main_sdf-student-manager.yml`) for continuous deployment to Azure Web App. However, this workflow is not supported anymore.
