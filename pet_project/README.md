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

## Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd pet_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements/base.txt
   ```

4. **Set up environment variables**
   Copy `.env.example` to `.env` and update the values:
   ```bash
   cp .env.example .env
   ```

5. **Database setup**
   - Create a PostgreSQL database
   - Update the `DATABASE_URL` in `.env`
   - Run migrations:
     ```bash
     alembic upgrade head
     ```

6. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

## API Documentation

Once the application is running, you can access:

- **Interactive API docs**: http://localhost:8000/docs
- **Alternative API docs**: http://localhost:8000/redoc

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black .
```

### Linting
```bash
flake8
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
