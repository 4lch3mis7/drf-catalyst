# DRF Catalyst: A High-Velocity Django REST Framework Starter Kit

## Introduction

DRF Catalyst is an opinionated boilerplate designed to jumpstart your REST API development with Django REST Framework. It provides a solid foundation with essential features and best practices, allowing you to focus on building your application's core logic from day one.

## Key Features

- **Django Environ**: Manage environment variables easily.
- **DRF Simple JWT**: JSON Web Token authentication for secure API access.
- **DRF YASG**: Automated generation of real Swagger/OpenAPI 2.0 specifications.
- **Django Filters**: Advanced filtering capabilities for Django REST Framework.
- **Django Phonenumber Field**: Phone number representation and validation.
- **Ruff**: Fast Python linter for code quality.

## Project Structure

```
drf_catalyst/
├── db.sqlite3
├── drf_catalyst
│   ├── __init__.py
│   ├── asgi.py
│   ├── exception_handler.py
│   ├── models.py
│   ├── permissions.py
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── settings.py
│   ├── swagger_router.py
│   ├── urls.py
│   └── wsgi.py
├── authusers
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── urls.py
│   ├── migrations
│   │   ├── __init__.py
│   ├── tests.py
│   ├── urls
│   │   ├── __init__.py
│   │   ├── users.py
│   ├── users
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
├── logs
│   ├── celery.log
│   ├── django.log
├── static
│   ├── admin
├── .env
├── .env.dist
├── .gitignore
├── .python-version
├── .vscode
│   ├── settings.json
├── Makefile
├── manage.py
├── pyproject.toml
├── README.md
├── uv.lock
```

## Project Setup

#### 1. Clone the repository and navigate to the project:
```bash
git clone https://github.com/4lch3mis7/drf-catalyst
cd drf-catalyst
```

### Start your project
```bash
export PROJECT_NAME=myproject
make startproject
```
