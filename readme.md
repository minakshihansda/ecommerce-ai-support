# E-Commerce AI Support

An AI-powered e-commerce customer support API built with FastAPI, SQLAlchemy, Alembic, JWT authentication, and Groq LLM.

## Features

* User registration and login
* JWT-based authentication
* Protected API endpoints
* Get current authenticated user
* Product listing and search by ID
* Cheapest product lookup
* Create, update, and delete products
* Product-category relationship
* Category creation and listing
* Get products by category
* Customer management
* Order management
* Order item management
* Support ticket management
* AI-powered customer support
* Groq LLM integration
* Database integration with SQLAlchemy
* Database migrations with Alembic
* Error handling and validation
* Interactive API documentation with Swagger UI

## Technologies

* Python
* FastAPI
* SQLAlchemy
* Alembic
* Pydantic
* JWT
* Passlib
* python-jose
* Groq
* python-dotenv
* Uvicorn

## Project Structure

```text
ecommerce-ai-support/
│
├── app/
│   ├── api/
│   │   ├── deps.py
│   │   └── v1/
│   │       ├── router.py
│   │       └── endpoints/
│   │           ├── auth.py
│   │           ├── categories.py
│   │           ├── chat.py
│   │           ├── customers.py
│   │           ├── health.py
│   │           ├── order_items.py
│   │           ├── orders.py
│   │           ├── products.py
│   │           ├── support_tickets.py
│   │           └── users.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── crud/
│   │   ├── category.py
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── order_item.py
│   │   ├── product.py
│   │   ├── support_ticket.py
│   │   └── user.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   ├── init_db.py
│   │   ├── session.py
│   │   └── models/
│   │       ├── category.py
│   │       ├── customer.py
│   │       ├── order.py
│   │       ├── order_item.py
│   │       ├── product.py
│   │       ├── support_ticket.py
│   │       └── user.py
│   │
│   ├── llm/
│   │   └── groq_provider.py
│   │
│   ├── schemas/
│   │   ├── category.py
│   │   ├── chat.py
│   │   ├── customer.py
│   │   ├── order.py
│   │   ├── order_item.py
│   │   ├── product.py
│   │   ├── support_ticket.py
│   │   └── user.py
│   │
│   ├── services/
│   │   └── chat_service.py
│   │
│   └── main.py
│
├── alembic/
│   └── versions/
│
├── alembic.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Run the Project

### 1. Create a virtual environment

```bash
py -m venv venv
```

### 2. Activate the virtual environment

Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Do not upload your real API key to GitHub.

### 5. Run database migrations

```bash
alembic upgrade head
```

### 6. Start the FastAPI server

```bash
py -m uvicorn app.main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Documentation

After starting the server, open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

Swagger UI allows you to view and test the API endpoints interactively.

## Authentication

The API uses JWT-based authentication.

### Register User

```http
POST /users
```

Example request:

```json
{
  "name": "John",
  "email": "john@example.com",
  "password": "password123"
}
```

### Login

```http
POST /login
```

Example request:

```json
{
  "email": "john@example.com",
  "password": "password123"
}
```

The response contains an access token:

```json
{
  "message": "Login successful",
  "access_token": "your_access_token",
  "token_type": "bearer",
  "user_id": 1
}
```

Use the access token in Swagger's **Authorize** button for protected endpoints.

### Current User

```http
GET /me
```

Returns information about the authenticated user.

## API Endpoints

### Health

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/health` | Check API health |

### Authentication and Users

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| POST   | `/users`           | Register a new user            |
| POST   | `/login`           | Login and receive JWT token    |
| GET    | `/me`              | Get current authenticated user |
| GET    | `/users/{user_id}` | Get user by ID                 |

### Products

| Method | Endpoint                          | Description                    |
| ------ | --------------------------------- | ------------------------------ |
| GET    | `/products`                       | Get all products               |
| GET    | `/products/{product_id}`          | Get product by ID              |
| GET    | `/products/cheapest`              | Find the cheapest product      |
| POST   | `/products`                       | Create a product               |
| PUT    | `/products/{product_id}`          | Update a product               |
| DELETE | `/products/{product_id}`          | Delete a product               |
| PUT    | `/products/{product_id}/category` | Assign a category to a product |

### Categories

| Method | Endpoint                             | Description                |
| ------ | ------------------------------------ | -------------------------- |
| POST   | `/categories`                        | Create a category          |
| GET    | `/categories`                        | Get all categories         |
| GET    | `/categories/{category_id}`          | Get category by ID         |
| GET    | `/categories/{category_id}/products` | Get products in a category |

### Customers

| Method | Endpoint                   | Description        |
| ------ | -------------------------- | ------------------ |
| POST   | `/customers`               | Create a customer  |
| GET    | `/customers/{customer_id}` | Get customer by ID |

### Orders

| Method | Endpoint             | Description     |
| ------ | -------------------- | --------------- |
| POST   | `/orders`            | Create an order |
| GET    | `/orders/{order_id}` | Get order by ID |

### Order Items

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/order-items`           | Create an order item |
| GET    | `/order-items/{item_id}` | Get order item by ID |

### Support Tickets

| Method | Endpoint                       | Description              |
| ------ | ------------------------------ | ------------------------ |
| POST   | `/support-tickets`             | Create a support ticket  |
| GET    | `/support-tickets/{ticket_id}` | Get support ticket by ID |

### AI Support

| Method | Endpoint | Description                                 |
| ------ | -------- | ------------------------------------------- |
| POST   | `/chat`  | Get an AI-powered customer support response |

## AI Chat

The `/chat` endpoint uses product information from the database and the Groq LLM to generate customer support responses.

Example request:

```json
{
  "message": "What is the cheapest product you have?"
}
```

Example response:

```json
{
  "answer": "The cheapest product is the USB-C Charger (ID: 3) at ₹799."
}
```

The `/chat` endpoint requires authentication.

## Database and Migrations

The project uses SQLAlchemy for database operations and Alembic for database schema migrations.

Run migrations with:

```bash
alembic upgrade head
```

## Security

* Passwords are stored as hashed values.
* JWT tokens are used for authentication.
* Protected endpoints require a valid Bearer token.
* The real Groq API key must remain in `.env`.
* `.env`, database files, virtual environments, and Python cache files are excluded through `.gitignore`.

## Project Purpose

This project demonstrates how FastAPI can be used to build an e-commerce customer support backend combining:

* REST APIs
* JWT authentication
* Database operations
* Product and category management
* Customer and order management
* Support ticket management
* SQLAlchemy ORM
* Alembic migrations
* AI-powered customer support
* Groq LLM integration

## Future Improvements

* Persistent chat history
* Product search and filtering
* Automated tests
* Frontend interface
* Role-based authorization
* API deployment to a cloud platform

## Author

Minakshi Hansda
