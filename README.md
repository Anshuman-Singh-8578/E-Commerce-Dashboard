# E-Commerce Dashboard

A command-line e-commerce management dashboard built with Python and Pandas. Runs directly in IDLE with no web server or database needed — all data is stored in CSV files.

---

## Folder Structure

```
ecommerce_dashboard/
├── main.py
├── README.md
├── data/
│   ├── products.csv
│   ├── customers.csv
│   ├── orders.csv
│   └── order_items.csv
└── modules/
    ├── __init__.py
    ├── file_handler.py
    ├── products.py
    ├── customers.py
    ├── orders.py
    └── reports.py
```

---

## Requirements

- Python 3.x
- Pandas library

Install pandas if you don't have it:

```
pip install pandas
```

---

## How to Run

1. Place all files in the folder structure shown above
2. Open `main.py` in IDLE
3. Press `F5` to run
4. Navigate using the number menus

---

## Features

### 1. Product Management
| Option | Description |
|--------|-------------|
| View All Products | Displays all products in a table |
| Search Product | Search by product name or ID |
| Add Product | Add a new product (ID auto-generated) |
| Update Product | Edit name, price, stock, category or brand |
| Delete Product | Remove a product by ID |

### 2. Customer Management
| Option | Description |
|--------|-------------|
| View All Customers | Displays all customers in a table |
| Search Customer | Search by name or email |
| Add Customer | Register a new customer (ID auto-generated) |
| Update Customer | Edit email, phone, city or tier |
| Delete Customer | Remove a customer by ID |

### 3. Order Management
| Option | Description |
|--------|-------------|
| View All Orders | Displays all orders in a table |
| View Order Details | Shows full order info + items for a given order ID |
| Place Order | Create a new order, checks and deducts stock automatically |
| Update Status | Change order status (Processing / Shipped / Delivered / Cancelled) |
| Cancel Order | Cancels an order and restores stock to products |

### 4. Reports & Analytics
| Option | Description |
|--------|-------------|
| Sales Summary | Total orders, revenue, average order value |
| Top Selling Products | Ranked by quantity sold or revenue |
| Low Stock Alert | Lists products below a stock threshold |
| Orders by Status | Count of orders per status |
| Revenue by Category | Total revenue grouped by product category |
| Export Report | Save filtered orders to a new CSV file |

---

## CSV File Structure

### products.csv
| Column | Description |
|--------|-------------|
| product_id | Unique ID (e.g. P001) |
| name | Product name |
| category | Product category |
| price | Price in ₹ |
| stock | Current stock quantity |
| status | InStock / LowStock / OutOfStock |
| brand | Brand name |
| sku | Stock keeping unit code |

### customers.csv
| Column | Description |
|--------|-------------|
| customer_id | Unique ID (e.g. C0001) |
| name | Full name |
| email | Email address |
| phone | Phone number |
| city | City |
| gender | Male / Female |
| dob | Date of birth (YYYY-MM-DD) |
| joined_date | Date customer was added |
| tier | Gold / Silver / Bronze |

### orders.csv
| Column | Description |
|--------|-------------|
| order_id | Unique ID (e.g. ORD00001) |
| customer_id | Links to customers.csv |
| order_date | Date order was placed (YYYY-MM-DD) |
| status | Processing / Shipped / Delivered / Cancelled |
| payment_method | UPI / Credit Card / Debit Card / COD / Net Banking / Wallet |
| total | Total order value in ₹ |
| delivery_date | Date delivered (blank if not yet delivered) |
| tracking_no | Courier tracking number |

### order_items.csv
| Column | Description |
|--------|-------------|
| order_id | Links to orders.csv |
| product_id | Links to products.csv |
| product_name | Product name at time of order |
| unit_price | Price per unit in ₹ |
| quantity | Quantity ordered |
| subtotal | unit_price x quantity |

---

## How Data Links Together

```
customers.csv
     │
     │ customer_id
     ▼
orders.csv ──── order_id ────▶ order_items.csv ──── product_id ────▶ products.csv
```

---

## Module Responsibilities

| File | Responsibility |
|------|---------------|
| `main.py` | Navigation — all menus and user input routing |
| `file_handler.py` | Reading and writing CSV files using pandas |
| `products.py` | All product-related functions |
| `customers.py` | All customer-related functions |
| `orders.py` | All order-related functions including stock management |
| `reports.py` | Analytics, summaries and CSV export |

---

## Important Notes

- **Stock is automatic** — placing an order deducts stock; cancelling an order restores it
- **Status is automatic** — stock status updates to `LowStock` when quantity drops below 20
- **IDs are auto-generated** — no need to manually type P098, C1001, ORD02732 etc.
- **All changes are saved** — every add, update or delete writes back to the CSV immediately
- **Cancelled and Delivered orders cannot be re-cancelled**

---

## Dataset

The project ships with a large realistic dataset generated using the Faker library:

| File | Records | Details |
|------|---------|---------|
| products.csv | 97 | 12 categories, real Indian brands, varied price ranges |
| customers.csv | 1,000 | Indian names, 100+ cities, joined 2022–2024 |
| orders.csv | 2,731 | Jan 2023 – Dec 2024, 6 payment methods |
| order_items.csv | 8,214 | 1–5 items per order with real subtotals |

### Product Categories
Bags, Beauty, Books, Clothing, Electronics, Footwear, Health, Home Decor, Kitchen, Sports, Stationery, Toys

### Customer Tiers
| Tier | Count |
|------|-------|
| Bronze | 440 |
| Silver | 353 |
| Gold | 207 |

### Order Status Breakdown
| Status | Count |
|--------|-------|
| Delivered | 2,050 |
| Shipped | 261 |
| Processing | 214 |
| Cancelled | 206 |

### Payment Methods
UPI, Credit Card, Debit Card, COD, Net Banking, Wallet

### Author
Anshuman Singh

BTech CSE student