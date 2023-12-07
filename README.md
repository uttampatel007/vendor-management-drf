# Vendor Management System with Performance Metrics

This is a Vendor Management System developed using Django and Django REST Framework. It manages vendor profiles, tracks purchase orders, and calculates vendor performance metrics.

## Setup Instructions

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/vendor-management-system.git
   cd vendor-management-system
   ```

2. Set up a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

The server will be running at `http://localhost:8000/`.

# API Endpoints

This document outlines the available endpoints for the Vendor Management System with Performance Metrics.

## Vendors

### Create a New Vendor
Create a new vendor profile.

- **POST /api/vendors/**
  - Parameters: JSON payload with vendor details.
  - Example: `POST /api/vendors/`

### List All Vendors
Retrieve a list of all vendors.

- **GET /api/vendors/**
  - Example: `GET /api/vendors/`

### Retrieve a Specific Vendor
Retrieve details of a specific vendor by ID.

- **GET /api/vendors/{vendor_id}/**
  - Example: `GET /api/vendors/123/`

### Update a Vendor
Update details of a specific vendor by ID.

- **PUT /api/vendors/{vendor_id}/**
  - Parameters: JSON payload with updated vendor details.
  - Example: `PUT /api/vendors/123/`

### Delete a Vendor
Delete a specific vendor by ID.

- **DELETE /api/vendors/{vendor_id}/**
  - Example: `DELETE /api/vendors/123/`

## Purchase Orders

### Create a Purchase Order
Create a new purchase order.

- **POST /api/purchase_orders/**
  - Parameters: JSON payload with purchase order details.
  - Example: `POST /api/purchase_orders/`

### List All Purchase Orders
Retrieve a list of all purchase orders with optional filtering by vendor.

- **GET /api/purchase_orders/**
  - Example: `GET /api/purchase_orders/`
  - Optional Filters: `GET /api/purchase_orders/?vendor_id=123`

### Retrieve a Specific Purchase Order
Retrieve details of a specific purchase order by ID.

- **GET /api/purchase_orders/{po_id}/**
  - Example: `GET /api/purchase_orders/456/`

### Update a Purchase Order
Update details of a specific purchase order by ID.

- **PUT /api/purchase_orders/{po_id}/**
  - Parameters: JSON payload with updated purchase order details.
  - Example: `PUT /api/purchase_orders/456/`

### Delete a Purchase Order
Delete a specific purchase order by ID.

- **DELETE /api/purchase_orders/{po_id}/**
  - Example: `DELETE /api/purchase_orders/456/`

### Acknowledge a Purchase Order
Acknowledge a specific purchase order by ID.

- **POST /api/purchase_orders/{po_id}/acknowledge/**
  - Example: `POST /api/purchase_orders/456/acknowledge/`

## Vendor Performance Metrics

### Retrieve Vendor Performance Metrics
Retrieve performance metrics for a specific vendor by ID.

- **GET /api/vendors/{vendor_id}/performance/**
  - Example: `GET /api/vendors/123/performance/`