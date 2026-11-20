import pandas as pd
from modules.file_handler import read_csv, write_csv

FILE = "data/products.csv"

def view_products():
    df = read_csv(FILE)
    print("\n" + df.to_string(index=False))

def search_product():
    df = read_csv(FILE)
    keyword = input("Enter product name or ID: ")
    result = df[df["name"].str.contains(keyword, case=False) | (df["product_id"] == keyword)]
    if result.empty:
        print("No products found.")
    else:
        print("\n" + result.to_string(index=False))

def add_product():
    df = read_csv(FILE)

    # Auto-generate next product ID
    last_id = df["product_id"].iloc[-1]          # e.g. P020
    next_num = int(last_id[1:]) + 1
    new_id = f"P{next_num:03d}"

    print(f"\nNew Product ID: {new_id}")
    name     = input("Product Name   : ")
    category = input("Category       : ")
    price    = float(input("Price (₹)      : "))
    stock    = int(input("Stock Quantity : "))
    brand    = input("Brand          : ")
    sku      = input("SKU            : ")

    status = "InStock" if stock >= 20 else "LowStock"

    new_row = {
        "product_id": new_id,
        "name"      : name,
        "category"  : category,
        "price"     : price,
        "stock"     : stock,
        "status"    : status,
        "brand"     : brand,
        "sku"       : sku
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    write_csv(df, FILE)
    print(f"Product {new_id} added successfully!")

def update_product():
    df = read_csv(FILE)
    pid = input("Enter Product ID to update: ").strip()

    if pid not in df["product_id"].values:
        print("Product not found.")
        return

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Price")
    print("3. Stock")
    print("4. Category")
    print("5. Brand")
    choice = input("Select: ")

    if choice == "1":
        df.loc[df["product_id"] == pid, "name"]     = input("New Name: ")
    elif choice == "2":
        df.loc[df["product_id"] == pid, "price"]    = float(input("New Price: "))
    elif choice == "3":
        new_stock = int(input("New Stock: "))
        df.loc[df["product_id"] == pid, "stock"]    = new_stock
        status = "InStock" if new_stock >= 20 else "LowStock"
        df.loc[df["product_id"] == pid, "status"]   = status
    elif choice == "4":
        df.loc[df["product_id"] == pid, "category"] = input("New Category: ")
    elif choice == "5":
        df.loc[df["product_id"] == pid, "brand"]    = input("New Brand: ")
    else:
        print("Invalid choice.")
        return

    write_csv(df, FILE)
    print("Product updated successfully!")

def delete_product():
    df = read_csv(FILE)
    pid = input("Enter Product ID to delete: ").strip()

    if pid not in df["product_id"].values:
        print("Product not found.")
        return

    confirm = input(f"Are you sure you want to delete {pid}? (yes/no): ")
    if confirm.lower() == "yes":
        df = df[df["product_id"] != pid]
        write_csv(df, FILE)
        print("Product deleted successfully!")
    else:
        print("Deletion cancelled.")
