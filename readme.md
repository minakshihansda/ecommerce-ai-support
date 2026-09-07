# E-Commerce AI Support

An AI-powered e-commerce customer support API built with FastAPI and Groq LLM.

## Features

* Product listing
* Product search by ID
* Cheapest product lookup
* AI-powered customer support
* Groq LLM integration
* Error handling

## Technologies

* Python
* FastAPI
* Pydantic
* Groq
* python-dotenv
* Uvicorn

## Project Structure

```text
ecommerce-ai-support/
│
├── app/
│   └── ...
│
├── main.py
├── readme.md
└── .gitignore
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

### 3. Start the FastAPI server

```bash
py -m uvicorn main:app --reload
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

You can use Swagger UI to test the available API endpoints.

## API Endpoints

| Method | Endpoint             | Description                 |
| ------ | -------------------- | --------------------------- |
| GET    | `/health`            | Check API health            |
| GET    | `/products`          | Get all products            |
| GET    | `/products/{id}`     | Get a product by ID         |
| GET    | `/products/cheapest` | Find the cheapest product   |
| POST   | `/chat`              | AI-powered customer support |
| POST   | `/compare`           | Compare products            |

## Environment Variables

For Groq LLM integration, create a `.env` file and add your API key:

```env
GROQ_API_KEY=your_api_key_here
```

Do not upload your real API key to GitHub.

## Project Purpose

This project demonstrates how FastAPI can be used to build an e-commerce customer support backend with product APIs and AI-powered customer assistance.

## Future Improvements

* Add a database for product storage
* Add user authentication
* Add order management
* Add frontend interface
* Add persistent chat history
* Deploy the API to a cloud platform

## Author

Minakshi Hansda
