 
# FastAPI Boilerplate - Industry Standard

## Introduction

Welcome to the FastAPI Boilerplate repository. This project serves as a launching pad for building high-performance, scalable web APIs that conform to industry standards. Our boilerplate incorporates the best practices of modern web development, ensuring that your application is not only fast and efficient but also maintainable and secure.

## Why FastAPI Boilerplate?

In the fast-paced world of web development, efficiency and speed are not just nice-to-haves; they're essential. The story of FastAPI Boilerplate begins with my quest for a framework that could keep up with the increasing demands for rapid, secure, and scalable web applications. I was working on a complex project with tight deadlines and needed a solution that would take care of the repetitive setup tasks without cutting corners on performance or security. 

FastAPI emerged as the beacon of modern web frameworks, offering high performance and easy-to-build APIs complemented by automatic interactive documentation. However, I noticed a gap. The initial setup, despite being straightforward, still consumed precious time - time that could be spent on building the unique aspects of my projects. 

That's when I decided to create the FastAPI Boilerplate. This project is the culmination of accumulated best practices, tools, and setups that I've fine-tuned over various projects. It is designed to be the perfect starting point, eliminating the boilerplate setup overhead, and empowering developers to launch into the actual building phase with confidence and speed. 

Our boilerplate is meticulously crafted to help you jumpstart your project without the hassle of setting up the foundational elements from scratch, ensuring that your application is not just fast and efficient but also secure and maintainable from the get-go.


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
