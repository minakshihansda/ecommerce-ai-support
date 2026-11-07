E-Commerce AI Support Assistant

An AI-powered E-Commerce Support System built using Python, FastAPI, PostgreSQL, SQLAlchemy, and Groq LLM. It provides product management, shopping cart, checkout, order tracking, and AI-powered customer support through a web interface.

Features

User Features

- User Registration and Login
- JWT-based Authentication
- Browse Available Products
- Add Products to Cart
- Update Cart Quantity
- Remove Products from Cart
- Checkout and Place Orders
- View My Orders
- Track Order Status
- Cancel Pending Orders
- AI-powered Customer Support Chatbot

Admin Features

- Admin Login and Dashboard
- Manage Order Status
- Update Payment Status
- View Order Information

Backend Features

- RESTful API Development
- Product and Category Management
- Customer and Order Management
- Order Item Management
- Support Ticket Management
- Database Integration
- Database Migrations
- Password Hashing
- Error Handling and Validation
- Swagger API Documentation

Technologies Used

Backend

- Python
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- JWT Authentication
- Passlib
- Groq LLM
- Uvicorn

Frontend

- HTML5
- CSS3
- JavaScript

Database

- PostgreSQL

Tools

- Visual Studio Code
- Git and GitHub
- Swagger UI

Project Structure

ecommerce-ai-support/
│
├── app/
│   ├── api/
│   ├── core/
│   ├── crud/
│   ├── db/
│   ├── llm/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── alembic/
│   └── versions/
│
├── frontend/
│   └── index.html
│
├── tests/
├── alembic.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md

Installation and Setup

1. Clone the Repository

git clone https://github.com/minakshihansda/ecommerce-ai-support.git

cd ecommerce-ai-support

2. Create a Virtual Environment

py -m venv venv

3. Activate Virtual Environment

Windows PowerShell:

venv\Scripts\activate

4. Install Dependencies

pip install -r requirements.txt

5. Configure Environment Variables

Create a ".env" file in the appropriate project configuration location and configure your database connection, secret key, and Groq API key.

Example:

DATABASE_URL=your_database_connection
SECRET_KEY=your_secret_key
GROQ_API_KEY=your_groq_api_key

Important: Never upload your real API keys or secret credentials to GitHub.

6. Run Database Migrations

alembic upgrade head

7. Start the Backend Server

uvicorn app.main:app --reload

Backend URL:

http://127.0.0.1:8000

8. Open the Frontend

Open "frontend/index.html" using the VS Code Live Server extension.

API Documentation

After starting the backend server, open Swagger UI:

http://127.0.0.1:8000/docs

Swagger UI allows users to explore and test the available API endpoints.

Main API Modules

Module| Description
Authentication| User registration and login
Users| User management
Products| Product listing and management
Categories| Product category management
Customers| Customer management
Orders| Order creation and management
Order Items| Order item management
Support Tickets| Customer support ticket management
Chat| AI-powered customer support
Health| Backend health check

AI Chatbot

The project integrates Groq LLM to provide AI-powered customer support.

The chatbot can use product information from the database to answer customer questions.

Example:

{
  "message": "What is the cheapest product you have?"
}

The chatbot provides a response based on the available product information.

Testing

Automated tests were executed using Pytest.

Test Result:

- Total Tests: 9
- Passed: 9
- Failed: 0

Security

- Passwords are stored in hashed form.
- JWT is used for authentication.
- Protected API endpoints require authentication.
- Secret credentials are stored in environment variables.
- Sensitive files are excluded through ".gitignore".

Project Purpose

The main purpose of this project is to develop an AI-powered e-commerce support system that combines:

- E-Commerce Operations
- REST API Development
- Database Management
- User Authentication
- Shopping Cart and Checkout
- Order Tracking
- Admin Order Management
- AI-powered Customer Support

Future Improvements

- Online Payment Gateway Integration
- Persistent Chat History
- Product Search and Filtering
- Email Notifications
- Cloud Deployment

Author

Minakshi Hansda


📄 License

This project was developed for educational purposes.