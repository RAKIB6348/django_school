# django_school

Django project for educational purposes.

## Project Structure

```
myproject/
├── manage.py
├── db.sqlite3
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── templates/          ← Custom template directory
```

## Settings

- **Framework**: Django 6.1
- **Database**: SQLite (`db.sqlite3`)
- **Installed Apps**: Django default apps only
- **Templates**: `myproject/templates/` directory configured in `settings.py`

## Recent Changes

- Added `templates/` directory for custom HTML templates
- Configured `DIRS` in `settings.py` to include the templates folder