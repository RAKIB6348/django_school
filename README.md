# django_school

Django school management system with user authentication and role-based dashboards.

## Project Structure

```
myproject/
├── manage.py
├── db.sqlite3
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   ├── wsgi.py
│   └── asgi.py
├── authentication/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── Admin/
│   │   └── dashboard.html
│   └── includes/
│       ├── header.html
│       ├── sidebar.html
│       └── footer.html
├── static/
└── media/
```

## Features

- Custom user model with role-based access (Admin, Teacher, Student)
- User authentication (Login/Logout)
- Admin dashboard with profile display
- Profile picture upload

## Setup

```bash
# Install dependencies
pip install django pillow

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run server
python manage.py runserver
```

## Settings

- **Framework**: Django 6.1
- **Database**: SQLite (`db.sqlite3`)
- **Custom User Model**: `authentication.CustomUser`
- **Templates**: `templates/` directory
- **Static Files**: `static/` directory
- **Media Files**: `media/` directory