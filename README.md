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

API Endpoints
Vendors
POST /api/vendors/: Create a new vendor.
GET /api/vendors/: List all vendors.
GET /api/vendors/{vendor_id}/: Retrieve details of a specific vendor.
PUT /api/vendors/{vendor_id}/: Update a vendor's details.
DELETE /api/vendors/{vendor_id}/: Delete a vendor.
Purchase Orders
POST /api/purchase_orders/: Create a purchase order.
GET /api/purchase_orders/: List all purchase orders with optional filtering by vendor.
GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.
PUT /api/purchase_orders/{po_id}/: Update a purchase order.
DELETE /api/purchase_orders/{po_id}/: Delete a purchase order.
POST /api/purchase_orders/{po_id}/acknowledge/: Acknowledge a purchase order.
Vendor Performance Metrics
GET /api/vendors/{vendor_id}/performance/: Retrieve performance metrics for a vendor.