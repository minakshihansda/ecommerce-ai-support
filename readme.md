# E-Commerce AI Support

An AI-powered e-commerce customer support API built with FastAPI, SQLAlchemy, Alembic, and Groq LLM.

## Features

* Product listing
* Product search by ID
* Cheapest product lookup
* Create, update, and delete products
* Product-category relationship
* Category creation and listing
* Get products by category
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
│   │       └── endpoints/
│   │           ├── categories.py
│   │           ├── chat.py
│   │           ├── health.py
│   │           ├── products.py
│   │           └── ...
│   │
│   ├── core/
│   │   └── config.py
│   │
│   ├── crud/
│   │   ├── category.py
│   │   └── product.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   └── models/
│   │       ├── category.py
│   │       └── product.py
│   │
│   ├── llm/
│   │   └── groq_provider.py
│   │
│   ├── schemas/
│   │   ├── category.py
│   │   └── product.py
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
├── .env
├── .gitignore
└── README.md
```

## Run the Project

### 1. Create and activate virtual environment

```bash
py -m venv venv
venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file and add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

Do not upload your real API key to GitHub.

### 4. Run database migrations

```bash
alembic upgrade head
```

### 5. Start the FastAPI server

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

Swagger UI allows you to view and test the available API endpoints interactively.

## API Endpoints

### Health

| Method | Endpoint  | Description      |
| ------ | --------- | ---------------- |
| GET    | `/health` | Check API health |

### Products

| Method | Endpoint                          | Description                    |
| ------ | --------------------------------- | ------------------------------ |
| GET    | `/products`                       | Get all products               |
| GET    | `/products/{product_id}`          | Get a product by ID            |
| GET    | `/products/cheapest`              | Find the cheapest product      |
| POST   | `/products`                       | Create a new product           |
| PUT    | `/products/{product_id}`          | Update a product               |
| DELETE | `/products/{product_id}`          | Delete a product               |
| PUT    | `/products/{product_id}/category` | Assign a category to a product |

### Categories

| Method | Endpoint                             | Description                          |
| ------ | ------------------------------------ | ------------------------------------ |
| POST   | `/categories`                        | Create a category                    |
| GET    | `/categories`                        | Get all categories                   |
| GET    | `/categories/{category_id}`          | Get a category by ID                 |
| GET    | `/categories/{category_id}/products` | Get products belonging to a category |

### AI Support

| Method | Endpoint | Description                                 |
| ------ | -------- | ------------------------------------------- |
| POST   | `/chat`  | Get an AI-powered customer support response |

## AI Chat

The `/chat` endpoint uses product information from the database to generate customer support responses through the Groq LLM.

Example request:

```json
{
  "message": "What is the cheapest product you have?"
}
```

Example response:

```json
{
  "answer": "The cheapest product we have is the USB-C Charger (ID 3) at ₹799."
}
```

## Database and Migrations

The project uses SQLAlchemy for database operations and Alembic for database schema migrations.

Example migration command:

```bash
alembic upgrade head
```

## Project Purpose

This project demonstrates how FastAPI can be used to build an e-commerce customer support backend combining:

* REST APIs
* Database operations
* Product and category management
* SQLAlchemy ORM
* Alembic migrations
* AI-powered customer support
* Groq LLM integration

## Future Improvements

* Add user authentication and authorization
* Add customer and order management
* Add support ticket management
* Add persistent chat history
* Add product search and filtering
* Add frontend interface
* Add automated tests
* Deploy the API to a cloud platform

## Author

Minakshi Hansda
