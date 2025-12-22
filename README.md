# Purchase Order Management System

## Overview

The Purchase Order Management System is a FastAPI-based application designed to manage purchase orders, suppliers, products, and users. It provides role-based access control to ensure secure and efficient management of procurement processes.

## Features

- **User Authentication and Authorization**: Role-based access control for users (e.g., Admin, Procurement, Finance, Warehouse).
- **Supplier Management**: Create and manage supplier details.
- **Product Management**: Add and manage product information.
- **Purchase Orders**: Create, approve, and receive purchase orders.
- **Audit Logs**: Track actions performed in the system.

## Project Structure

```
.
├── purchase.db
├── README.md
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── audit_log.py
│   │   ├── product.py
│   │   ├── purchase_item.py
│   │   ├── purchase_order.py
│   │   ├── supplier.py
│   │   ├── users.py
│   ├── routes/
│   │   ├── products.py
│   │   ├── purchase_orders.py
│   │   ├── suppliers.py
│   │   ├── users.py
│   ├── schemas/
│   │   ├── product.py
│   │   ├── purchase_order.py
│   │   ├── supplier.py
│   │   ├── users.py
│   ├── utils/
│       ├── jwt_handler.py
```

## Installation

### Prerequisites

- Python 3.10+
- SQLite (or any other database supported by SQLAlchemy)

### Steps

1. Clone the repository:

   ```bash
   git clone purchase_order_system_fastapi.git
   cd purchase_order_system_fastapi
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:

   - Create a `.env` file in the root directory with the following content:
     ```env
     SQLALCHEMY_DATABASE_URI=sqlite:///purchase.db
     SECRET_KEY=mysecretkey
     ALGORITHM=HS256
     ```

5. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the application at `http://127.0.0.1:8000`.

## API Endpoints

### Authentication

- **POST** `/login`: Login and obtain an access token.
- **POST** `/register`: Register a new user.

### Users

- **GET** `/me`: Get details of the currently logged-in user.

### Suppliers

- **POST** `/suppliers`: Create a new supplier (Admin role required).

### Products

- **POST** `/products`: Create a new product (Admin role required).

### Purchase Orders

- **POST** `/purchase-orders`: Create a new purchase order (Procurement role required).
- **PUT** `/purchase-orders/{po_id}/approve`: Approve a purchase order (Finance role required).
- **PUT** `/purchase-orders/{po_id}/receive`: Mark a purchase order as received (Warehouse role required).

## Project Configuration

### Configuration File

The application uses a `.env` file for configuration. Key settings include:

- `SQLALCHEMY_DATABASE_URI`: Database connection string.
- `SECRET_KEY`: Secret key for JWT authentication.
- `ALGORITHM`: Algorithm used for JWT encoding.

### Database

The application uses SQLAlchemy for ORM and SQLite as the default database. The database schema is automatically created on application startup.

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Uvicorn](https://www.uvicorn.org/)
