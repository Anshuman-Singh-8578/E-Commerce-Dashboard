import pandas as pd
from datetime import date
from modules.file_handler import read_csv, write_csv

ORDERS_FILE   = "data/orders.csv"
ITEMS_FILE    = "data/order_items.csv"
PRODUCTS_FILE = "data/products.csv"

def view_orders():
    df = read_csv(ORDERS_FILE)
    print("\n" + df.to_string(index=False))

def view_order_details():
    orders = read_csv(ORDERS_FILE)
    items  = read_csv(ITEMS_FILE)
    oid    = input("Enter Order ID: ").strip()

    order = orders[orders["order_id"] == oid]
    if order.empty:
        print("Order not found.")
        return

    print("\n--- Order Info ---")
    print(order.to_string(index=False))
    print("\n--- Order Items ---")
    print(items[items["order_id"] == oid].to_string(index=False))

def place_order():
    orders   = read_csv(ORDERS_FILE)
    items    = read_csv(ITEMS_FILE)
    products = read_csv(PRODUCTS_FILE)

    # Auto-generate next order ID
    last_id  = orders["order_id"].iloc[-1]        # e.g. ORD025
    next_num = int(last_id[3:]) + 1
    new_oid  = f"ORD{next_num:03d}"

    cid = input("Enter Customer ID: ").strip()

    order_items_list = []
    total = 0

    while True:
        pid = input("Enter Product ID (or 'done' to finish): ").strip()
        if pid.lower() == "done":
            break

        product_row = products[products["product_id"] == pid]
        if product_row.empty:
            print("Product not found. Try again.")
            continue

        stock = int(product_row["stock"].values[0])
        price = float(product_row["price"].values[0])
        pname = product_row["name"].values[0]
        qty   = int(input(f"Quantity (available: {stock}): "))

        if qty > stock:
            print(f"Not enough stock. Only {stock} available.")
            continue

        subtotal = price * qty
        total   += subtotal

        # Deduct stock
        products.loc[products["product_id"] == pid, "stock"] -= qty
        new_stock = int(products.loc[products["product_id"] == pid, "stock"].values[0])
        status = "InStock" if new_stock >= 20 else ("LowStock" if new_stock > 0 else "OutOfStock")
        products.loc[products["product_id"] == pid, "status"] = status

        order_items_list.append({
            "order_id"    : new_oid,
            "product_id"  : pid,
            "product_name": pname,
            "unit_price"  : price,
            "quantity"    : qty,
            "subtotal"    : subtotal
        })
        print(f"Added: {pname} x{qty} = ₹{subtotal}")

    if not order_items_list:
        print("No items added. Order cancelled.")
        return

    payment = input("Payment Method (UPI/Credit Card/Debit Card/COD/Net Banking): ")

    new_order = {
        "order_id"      : new_oid,
        "customer_id"   : cid,
        "order_date"    : str(date.today()),
        "status"        : "Processing",
        "payment_method": payment,
        "total"         : total,
        "delivery_date" : "",
        "tracking_no"   : ""
    }

    orders   = pd.concat([orders,   pd.DataFrame([new_order])],      ignore_index=True)
    items    = pd.concat([items,    pd.DataFrame(order_items_list)],  ignore_index=True)

    write_csv(orders,   ORDERS_FILE)
    write_csv(items,    ITEMS_FILE)
    write_csv(products, PRODUCTS_FILE)

    print(f"\nOrder {new_oid} placed successfully! Total: ₹{total}")

def update_status():
    df  = read_csv(ORDERS_FILE)
    oid = input("Enter Order ID: ").strip()

    if oid not in df["order_id"].values:
        print("Order not found.")
        return

    current = df.loc[df["order_id"] == oid, "status"].values[0]
    print(f"Current status: {current}")
    new_status = input("New status (Processing/Shipped/Delivered/Cancelled): ").strip()

    df.loc[df["order_id"] == oid, "status"] = new_status

    if new_status == "Delivered":
        df.loc[df["order_id"] == oid, "delivery_date"] = str(date.today())

    write_csv(df, ORDERS_FILE)
    print("Order status updated successfully!")

def cancel_order():
    orders   = read_csv(ORDERS_FILE)
    items    = read_csv(ITEMS_FILE)
    products = read_csv(PRODUCTS_FILE)

    oid = input("Enter Order ID to cancel: ").strip()

    if oid not in orders["order_id"].values:
        print("Order not found.")
        return

    current = orders.loc[orders["order_id"] == oid, "status"].values[0]
    if current == "Cancelled":
        print("Order is already cancelled.")
        return
    if current == "Delivered":
        print("Cannot cancel a delivered order.")
        return

    confirm = input(f"Are you sure you want to cancel {oid}? (yes/no): ")
    if confirm.lower() != "yes":
        print("Cancellation aborted.")
        return

    # Restore stock for each item in the order
    order_items = items[items["order_id"] == oid]
    for _, row in order_items.iterrows():
        pid = row["product_id"]
        qty = row["quantity"]
        products.loc[products["product_id"] == pid, "stock"] += qty
        new_stock = int(products.loc[products["product_id"] == pid, "stock"].values[0])
        status = "InStock" if new_stock >= 20 else "LowStock"
        products.loc[products["product_id"] == pid, "status"] = status

    orders.loc[orders["order_id"] == oid, "status"] = "Cancelled"

    write_csv(orders,   ORDERS_FILE)
    write_csv(products, PRODUCTS_FILE)
    print(f"Order {oid} cancelled and stock restored successfully!")
