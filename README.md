
Phimart - E-commerce API

Phimart is a Django REST Framework (DRF) based backend API for an E-commerce platform.
It provides endpoints for Products, Categories, Carts, and Orders, with JWT authentication using Djoser.
Interactive API documentation is included using Swagger (drf_yasg).

🚀 Features

JWT Authentication with Djoser

User Registration & Login

Product & Category Management

Shopping Cart with Cart Items

Order Management

Interactive API Documentation (Swagger + Redoc)

🛠 Technologies Used

Backend: Django, Django REST Framework

Authentication: Djoser + JWT

Database: SQLite (default), PostgreSQL (recommended)

API Docs: drf_yasg (Swagger + Redoc)

Language: Python 3.11+

⚙️ Installation

Clone the repository

git clone https://github.com/your-username/phimart.git
cd phimart


Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Install dependencies

pip install -r requirements.txt


Apply migrations

python manage.py migrate


Create a superuser

python manage.py createsuperuser


Run the server

python manage.py runserver

📑 API Endpoints
🛍 Products & Categories

GET /api/products/ → List all products

GET /api/products/{id}/ → Retrieve product details

GET /api/categories/ → List categories

🛒 Cart

POST /api/carts/ → Create a cart

GET /api/carts/{id}/ → Retrieve cart details

POST /api/carts/{cart_id}/items/ → Add item to cart

PATCH /api/carts/{cart_id}/items/{id}/ → Update cart item

DELETE /api/carts/{cart_id}/items/{id}/ → Remove cart item

📦 Orders

POST /api/orders/ → Create an order

GET /api/orders/ → List user orders

GET /api/orders/{id}/ → Retrieve order details

🔑 Authentication (JWT - Djoser)

POST /auth/users/ → Register new user

POST /auth/jwt/create/ → Login (get tokens)

POST /auth/jwt/refresh/ → Refresh token

POST /auth/jwt/verify/ → Verify token

📖 API Documentation

Swagger UI: http://localhost:8000/swagger/

Redoc UI: http://localhost:8000/redoc/

🌍 Environment Variables

Create a .env file in the project root:

SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DATABASE_URL=sqlite:///db.sqlite3   # or your PostgreSQL connection string

🚀 Deployment (Optional)

Phimart can be deployed to Heroku, Railway, Render, or Docker.
(PostgreSQL is recommended for production).

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by Your Name

GitHub: your-username

LinkedIn: your-linkedin