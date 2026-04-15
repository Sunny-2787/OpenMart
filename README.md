# 🛒 E-Commerce API (Django REST Framework)

A fully functional backend API for an E-Commerce system built using **Django REST Framework (DRF)**. This project includes core features like product management, categories, cart system, orders, and secure authentication using JWT.

---

## 🚀 Features

* 🔐 JWT Authentication (Login / Register)
* 🛍️ Product Management
* 📂 Category Management
* 🛒 Cart System
* 📦 Order Processing
* 📑 API Documentation with Swagger (DRF-YASG)

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework (DRF)
* JWT Authentication (djangorestframework-simplejwt / jossar)
* DRF-YASG (Swagger UI)

---

## 📁 API Endpoints

### 🔐 Authentication (JWT)

| Method | Endpoint            | Description   |
| ------ | ------------------- | ------------- |
| POST   | /api/token/         | Get JWT token |
| POST   | /api/token/refresh/ | Refresh token |

---

### 📦 Products

| Method | Endpoint        | Description       |
| ------ | --------------- | ----------------- |
| GET    | /products/      | List all products |
| POST   | /products/      | Create product    |
| GET    | /products/{id}/ | Retrieve product  |
| PUT    | /products/{id}/ | Update product    |
| DELETE | /products/{id}/ | Delete product    |

---

### 📂 Categories

| Method | Endpoint          | Description       |
| ------ | ----------------- | ----------------- |
| GET    | /categories/      | List categories   |
| POST   | /categories/      | Create category   |
| GET    | /categories/{id}/ | Retrieve category |
| PUT    | /categories/{id}/ | Update category   |
| DELETE | /categories/{id}/ | Delete category   |

---

### 🛒 Cart

| Method | Endpoint    | Description      |
| ------ | ----------- | ---------------- |
| GET    | /cart/      | View cart        |
| POST   | /cart/      | Add item to cart |
| PATCH  | /cart/{id}/ | Update cart item |
| DELETE | /cart/{id}/ | Remove item      |

---

### 📦 Orders

| Method | Endpoint      | Description      |
| ------ | ------------- | ---------------- |
| GET    | /orders/      | List user orders |
| POST   | /orders/      | Create order     |
| GET    | /orders/{id}/ | Order details    |

---

## 📄 API Documentation

Swagger UI is available for testing and exploring APIs:

```
/swagger/
/redoc/
```

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/yourusername/ecommerce-api.git

# Go to project folder
cd ecommerce-api

# Create virtual environment
python -m venv env

# Activate environment
source env/bin/activate   # Linux/Mac
env\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Run server
python manage.py runserver
```

---

## 🔑 Authentication Setup

* Uses JWT authentication
* Include token in headers:

```
Authorization: Bearer <your_access_token>
```

---

## 🧪 Testing

You can test endpoints using:

* Swagger UI
* Postman
* Curl

---

## 📌 Notes

* Only authenticated users can access cart and orders
* Admin users can manage products and categories
* Pagination and filtering can be added for scalability

---

## 👨‍💻 Author

**Sunny**

---

## 📜 License

This project is open-source and available under the MIT License.
