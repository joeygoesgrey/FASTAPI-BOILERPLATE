# FastAPI Boilerplate - Industry Standard

## Introduction

Welcome to the FastAPI Boilerplate repository. This project serves as a launching pad for building high-performance, scalable web APIs that conform to industry standards. My boilerplate incorporates the best practices of modern web development, ensuring that your application is not only fast and efficient but also maintainable and secure.

## Why FastAPI Boilerplate?

Modern web applications demand modern solutions. FastAPI is a contemporary framework that offers high performance, easy-to-build APIs with automatic interactive documentation. My boilerplate is designed to help you jumpstart your project without the hassle of setting up the foundational elements from scratch.

### Features

- **Asynchronous Support**: Harness the full power of async programming to handle a large number of requests simultaneously.
- **Containerization with Docker**: Package your application with all its dependencies in a Docker container.
- **ORM with SQLAlchemy**: Interact with databases easily with the SQLAlchemy ORM integrated into the boilerplate.
- **Automatic Migration with Alembic**: Keep your database schema in sync with your models through Alembic migrations.
- **Secure Authentication**: Built-in OAuth2 password and bearer with JWT tokens for secure and stateless authentication.
- **Dependency Management with Pipenv**: Manage your dependencies and environment with the robust packaging tool, Pipenv.

## Getting Started

### Prerequisites

- Python 3.6+
- Docker
- Pipenv


### Project Structure & Guide


<!-- ├── alembic.ini                                # File: Configuration file for Alembic (database migrations)
├── app/                                       # Directory: Main application directory
│   ├── api/                                   # Directory: API routes and endpoints
│   │   ├── auth_routers/                      # Directory: Authentication-related routes
│   │   │   ├── __init__.py                    # File: Initializes Python package for auth_routers
│   │   │   └── routes.py                      # File: Authentication routes definitions
│   │   └── __init__.py                        # File: Initializes Python package for the API module
│   ├── core/                                  # Directory: Core application components (configurations, database connection, etc.)
│   │   ├── config.py                          # File: Configuration settings (database URLs, secrets)
│   │   ├── db/                                # Directory: Database-related modules (session management, mixins, transactions)
│   │   │   ├── __init__.py                    # File: Initializes Python package for the db module
│   │   │   ├── mixins/                        # Directory: Mixins for database models (e.g., timestamp mixin)
│   │   │   │   ├── __init__.py                # File: Initializes Python package for mixins
│   │   │   │   └── timestamp_mixin.py         # File: Mixin for adding timestamp fields to models if inherited
│   │   │   ├── session.py                     # File: Database session management
│   │   │   ├── standalone_session.py          # File: Standalone session management for async tasks
│   │   │   └── transactional.py               # File: Transactional decorators for database operations
│   │   ├── dependencies/                      # Directory: Dependency-related modules (logging, permissions)
│   │   │   ├── __init__.py                    # File: Initializes Python package for dependencies
│   │   │   ├── logging.py                     # File: Logging dependencies
│   │   │   └── permission.py                  # File: Permission checking dependencies
│   │   ├── exceptions/                        # Directory: Custom exceptions
│   │   │   ├── base.py                        # File: Base exception class
│   │   │   ├── __init__.py                    # File: Initializes Python package for exceptions
│   │   │   └── token.py                       # File: Token-related exceptions
│   │   ├── __init__.py                        # File: Initializes Python package for the core module
│   │   ├── middlewares/                       # Directory: Middleware components (authentication, logging, SQLAlchemy session management)
│   │   │   ├── authentication.py              # File: Authentication middleware
│   │   │   ├── __init__.py                    # File: Initializes Python package for middlewares
│   │   │   ├── response_log.py                # File: Response logging middleware
│   │   │   └── sqlalchemy.py                  # File: SQLAlchemy session middleware
│   │   ├── repository/                        # Directory: Repository layer for abstracting database operations
│   │   │   ├── base.py                        # File: Base repository class
│   │   │   ├── enum.py                        # File: Enumerations used in repositories
│   │   │   └── __init__.py                    # File: Initializes Python package for the repository module
│   │   └── utils/                             # Directory: Utility functions and helpers
│   │       ├── __init__.py                    # File: Initializes Python package for utils
│   │       ├── password_utils.py              # File: Password-related utilities
│   │       ├── token_helper.py                # File: Token generation and validation helpers
│   │       └── validator.py                   # File: Input validation helpers
│   ├── __init__.py                            # File: Initializes Python package for the app module
│   ├── models/                                # Directory: Database models
│   │   ├── __init__.py                        # File: Initializes Python package for models
│   │   └── models.py                          # File: Model definitions
│   ├── schemas/                               # Directory: Pydantic schemas for request and response validation
│   │   ├── api_main_schemas/                  # Directory: Main API schemas
│   │   │   ├── __init__.py                    # File: Initializes Python package for api_main_schemas
│   │   │   └── schemas.py                     # File: Schema definitions for main API
│   │   └── auth_schemas/                      # Directory: Authentication-related schemas
│   │       ├── __init__.py                    # File: Initializes Python package for auth_schemas
│   │       └── schema.py                      # File: Schema definitions for authentication
│   └── server.py                              # File: ASGI server configuration
├── docker-compose.yml                         # File: Docker Compose configuration for local development
├── Dockerfile                                 # File: Dockerfile for containerizing the application
├── main.py                                    # File: Entry point for the FastAPI application
├── migrations/                                # Directory: Database migration scripts (managed by Alembic)
│   ├── env.py                                 # File: Alembic environment setup
│   ├── README                                 # File: Instructions for migration management
│   ├── script.py.mako                         # File: Template for generating Alembic migration files
│   └── versions/                              # Directory: Directory for migration version scripts
├── Pipfile                                    # File: Pipenv file for managing dependencies
├── Pipfile.lock                               # File: Lockfile for dependencies, ensures repeatable installations
├── README.md                                  # File: Project README with instructions and information
├── tests/                                     # Directory: Unit and integration tests
│   └── __init__.py                            # File: Initializes Python package for tests
├── TODO-FASTAPI                               # File: File for tracking TODO items for the project
└── Uploads/                                   # Directory: Directory for storing uploaded files (if any) -->


### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/joeygoesgrey/FASTAPI-BOILERPLATE.git
   ```

2. **Navigate to the Project Directory**

   After cloning the repository, navigate to the project directory:

   ```bash
   cd FASTAPI-BOILERPLATE
   ```

3. **Install Dependencies**

   Install the necessary dependencies using Pipenv:

   ```bash
   pipenv install
   ```

4. **Set Environment Variables**

   Configure your environment variables by updating them with your specific settings.

5. **Run with Docker Compose**

   Build and start the services using Docker Compose:

   ```bash
   docker-compose up --build
   ```

6. **Perform Database Migrations**

   Initialize your database and perform migrations with the following command:

   ```bash
   pipenv run alembic upgrade head
   ```

7. **Start the FastAPI Server**

   Your application will be accessible at `http://localhost:8080`, and the API documentation can be found at `http://localhost:8080/docs`.

   ```bash
   pipenv run python3 main.py --env dev
   ```

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository, make your changes, and submit a pull request.

## License

This project is open-sourced under the MIT License. For more details, see the LICENSE.md file in this repository.

Happy Coding!
