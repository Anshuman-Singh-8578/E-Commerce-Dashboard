import pandas as pd
from modules.file_handler import read_csv

def sales_summary():
    orders = read_csv("data/orders.csv")
    delivered = orders[orders["status"] == "Delivered"]

    print("\n===== SALES SUMMARY =====")
    print(f"Total Orders     : {len(orders)}")
    print(f"Delivered Orders : {len(delivered)}")
    print(f"Total Revenue    : ₹{delivered['total'].sum():,.2f}")
    print(f"Avg Order Value  : ₹{delivered['total'].mean():,.2f}")
    print(f"Cancelled Orders : {len(orders[orders['status'] == 'Cancelled'])}")
    print(f"Pending/Shipping : {len(orders[orders['status'].isin(['Processing', 'Shipped'])])}")

def top_products():
    items = read_csv("data/order_items.csv")
    n = input("Show top how many products? (default 5): ").strip()
    n = int(n) if n.isdigit() else 5

    by_qty = items.groupby("product_name")["quantity"].sum().sort_values(ascending=False).head(n)
    by_rev = items.groupby("product_name")["subtotal"].sum().sort_values(ascending=False).head(n)

    print(f"\n--- Top {n} by Quantity Sold ---")
    print(by_qty.to_string())
    print(f"\n--- Top {n} by Revenue ---")
    print(by_rev.to_string())

def low_stock_alert():
    products  = read_csv("data/products.csv")
    threshold = input("Stock threshold (default 20): ").strip()
    threshold = int(threshold) if threshold.isdigit() else 20

    low = products[products["stock"] < threshold]
    if low.empty:
        print(f"All products have stock above {threshold}.")
    else:
        print(f"\n--- Products with stock below {threshold} ---")
        print(low[["product_id", "name", "stock", "status"]].to_string(index=False))

def orders_by_status():
    orders = read_csv("data/orders.csv")
    print("\n--- Orders by Status ---")
    print(orders["status"].value_counts().to_string())

def revenue_by_category():
    items    = read_csv("data/order_items.csv")
    products = read_csv("data/products.csv")
    merged   = items.merge(products[["product_id", "category"]], on="product_id")
    result   = merged.groupby("category")["subtotal"].sum().sort_values(ascending=False)
    print("\n--- Revenue by Category ---")
    print(result.to_string())

def export_report():
    orders = read_csv("data/orders.csv")
    print("\nExport Options:")
    print("1. All Orders")
    print("2. By Status")
    print("3. By Date Range")
    choice = input("Select: ").strip()

    if choice == "1":
        df = orders

    elif choice == "2":
        status = input("Status (Delivered/Shipped/Processing/Cancelled): ").strip()
        df = orders[orders["status"] == status]

    elif choice == "3":
        start = input("Start date (YYYY-MM-DD): ").strip()
        end   = input("End date   (YYYY-MM-DD): ").strip()
        df    = orders[(orders["order_date"] >= start) & (orders["order_date"] <= end)]

    else:
        print("Invalid choice.")
        return

    if df.empty:
        print("No data found for the selected filter.")
        return

    filename = input("Enter filename (without .csv): ").strip()
    filepath = f"data/{filename}.csv"
    df.to_csv(filepath, index=False)
    print(f"Report exported to {filepath} ({len(df)} rows)")
