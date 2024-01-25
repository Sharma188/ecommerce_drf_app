# ecommerce_drf_app

This is a Django Rest Framework (DRF) application for an e-commerce platform. The platform includes user authentication, product and category management, cart and order management, and an admin dashboard.

## Features

### User Authentication
- User authentication with different roles (admin and regular users).
- Admins can perform CRUD operations on products and categories.

### Product and Category Management
- Models for products and categories with appropriate fields (name, description, price, image, etc.).
- Products can belong to one or more categories (flexible limit from 1 to n).

### User Interface
- Basic interfaces for browsing products and categories.
- End users can add products to a cart, manage the cart (add, remove items), and place orders.

### Cart and Order Management
- Cart system for users to add and remove products.
- Users can review the cart, modify quantities, and proceed to checkout to place orders.

### Admin Dashboard
- Admins have access to a dashboard to manage products and categories.
- CRUD functionalities for adding, editing, and deleting products and categories.
- Products can be added using csv upload (Bulk insert) in API.

## Installation

1. Clone the repository: `https://github.com/Sharma188/ecommerce_drf_app.git`
2. Install the requirements: `pip install -r requirements.txt`
3. Migrate the database: `python manage.py migrate`
4. Run the server: `python manage.py runserver`

## Usage

### User Registration and Login
- Endpoint: `/api/user/`
- Method: `POST`
- Data: `{"username": "yourusername", "password": "yourpassword"}`

### Browsing Products and Categories
- Endpoint: `/api/products/` and `/api/categories/`
- Method: `GET`

### Adding Products to a Cart
- Endpoint: `/api/cart/`
- Method: `POST`
- Data: `{"product": product_id, "quantity": quantity}`

### Managing the Cart
- Endpoint: `/api/cart/cart_id/`
- Method: `PUT` or `PATCH`
- Data: `{"quantity": new_quantity}`

### Placing Orders
- Endpoint: `/api/orders/`
- Method: `POST`
- Data: `{"cart": cart_id}`

### Admin Dashboard
- Endpoint: `/admin/`
