# Pet Project API

A comprehensive FastAPI-based backend application with authentication, database integration, and message queue support.

## Project Structure

```
pet_project/
├── .env                    # Environment variables
├── requirements/           # Project dependencies
│   └── base.txt            # Main requirements
└── app/                    # Application package
    ├── __init__.py
    ├── main.py             # FastAPI application entry point
    │
    ├── api/                # API routes
    │   └── v1/             # API version 1
    │       ├── endpoints/  # API endpoints
    │       └── api.py      # API router
    │
    ├── config/             # Configuration
    │   └── settings.py     # Application settings
    │
    ├── core/               # Core functionality
    │   └── security.py     # Authentication and security
    │
    ├── database/           # Database configuration
    │   └── __init__.py
    │
    ├── models/             # Database models
    │   └── user.py         # User and Worker models
    │
    ├── schemas/            # Pydantic models
    │   └── user.py         # Request/response schemas
    │
    └── workers/            # Background workers
        └── rabbitmq.py     # RabbitMQ consumer/producer
```

## Features

- **Authentication**: JWT-based authentication system
- **Database**: SQLAlchemy ORM with async support
- **API**: RESTful endpoints with versioning
- **Message Queue**: RabbitMQ integration for async tasks
- **Testing**: Pytest setup for unit and integration tests
- **Configuration**: Environment-based configuration

