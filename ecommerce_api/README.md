# E-commerce Product API

This project is a backend API for an e-commerce platform, built with **Django** and **Django REST Framework (DRF)**. It supports product management, user authentication, and product search functionality. The API is designed to mimic the responsibilities of a backend developer in a real-world e-commerce environment.

---

    ### 1. Features

    ### 1. Product Management (CRUD)
    - Create, Read, Update, and Delete (CRUD) products.
    - Product attributes include:
    - **Name**: The name of the product.
    - **Description**: A detailed description of the product.
    - **Price**: The product's price.
    - **Category**: The category to which the product belongs (e.g., Electronics, Clothing).
    - **Stock Quantity**: The available quantity in stock.
    - **Image URL**: A link to the product image.
    - **Created Date**: Automatically generated timestamp for product creation.
    - Validation for required fields like `Name`, `Price`, and `Stock Quantity`.

---

    ### 2. User Management (CRUD)
    - Manage users who can perform CRUD operations on products.
    - User attributes include:
    - **Username** (unique)
    - **Email** (unique)
    - **Password**
    - **Authentication Required**: Only authenticated users can manage products. 
    - Support for custom user models with extensibility.

---

    ### 3. Product Search
    - Search for products by `Name` or `Category`.
    - Supports partial matches in product names for flexible search results.
    - Pagination is implemented to handle large datasets efficiently.

---

    ### 4. Product View
    - Retrieve a list of all products or view individual product details.
    - Optional filters:
    - By **Category**
    - By **Price Range**
    - By **Stock Availability**
    - Includes full product details in the response.

---

    ### 5. Authentication
    - Uses Django’s built-in authentication system.
    - Optionally supports token-based authentication (JWT) for secure API access.

---

    ### 6. Database and ORM
    - Database interaction is handled using Django ORM.
    - Models:
    - **Product**: Represents e-commerce products.
    - **User**: Custom user model for authentication and user management.
    - Relationships: Each product is associated with a category.

---

    ### 7. Deployment
    - Deployed using **Heroku** or **PythonAnywhere** for public accessibility.
    - Includes configuration for production environments.

---

## Installation and Setup

1. **Clone the Repository**:

```bash

   git clone https://github.com/your-username/ecommerce-api.git
   cd ecommerce-api
Create a Virtual Environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # For Linux/MacOS
venv\Scripts\activate     # For Windows
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Run Migrations:

bash
Copy code
python manage.py makemigrations
python manage.py migrate
Create a Superuser (for accessing the admin panel):

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
API Endpoints
Authentication
Login: /api/token/ (POST)
Refresh Token: /api/token/refresh/ (POST)
Products
List All Products: /api/products/ (GET)
Product Details: /api/products/<id>/ (GET)
Create Product: /api/products/ (POST)
Update Product: /api/products/<id>/ (PUT)
Delete Product: /api/products/<id>/ (DELETE)
Search
Search Products: /api/products/search/?query=<query> (GET)
Technologies Used
Backend Framework: Django, Django REST Framework
Database: SQLite (default), with options to use PostgreSQL in production
Authentication: Django Authentication, optional JWT
Hosting: Heroku or PythonAnywhere
Future Enhancements
Implement order management, including stock reduction upon order placement.
Add detailed user roles and permissions for enhanced security.
Improve search functionality with additional filters.
