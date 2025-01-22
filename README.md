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
myproject/
├── authusers
│   ├── admin.py
│   ├── apps.py
│   ├── auth
│   │   └── urls.py
│   ├── models.py
│   ├── tests.py
│   └── users
│       ├── serializers.py
│       ├── urls.py
│       └── views.py
├── myproject
│   ├── asgi.py
│   ├── exception_handler.py
│   ├── models.py
│   ├── permissions.py
│   ├── response_handler.py
│   ├── settings
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── settings.py
│   ├── swagger_router.py
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── manage.py
├── pyproject.toml
├── README.md
└── uv.lock
```

## Project Setup

#### Create a new project directory:
```bash
mkdir myproject && cd myproject
```

#### 1. Clone the repository and navigate to the project:
```bash
git clone https://github.com/4lch3mis7/drf-catalyst .
```

### 2. Start your project
```bash
make --file=drf-catalyst/Makefile PROJECT_NAME=myproject
```
