import pandas as pd
from modules.file_handler import read_csv, write_csv

FILE = "data/customers.csv"

def view_customers():
    df = read_csv(FILE)
    print("\n" + df.to_string(index=False))

def search_customer():
    df = read_csv(FILE)
    keyword = input("Enter name or email: ")
    result = df[df["name"].str.contains(keyword, case=False) |
                df["email"].str.contains(keyword, case=False)]
    if result.empty:
        print("No customers found.")
    else:
        print("\n" + result.to_string(index=False))

def add_customer():
    df = read_csv(FILE)

    # Auto-generate next customer ID
    last_id  = df["customer_id"].iloc[-1]         # e.g. C015
    next_num = int(last_id[1:]) + 1
    new_id   = f"C{next_num:03d}"

    print(f"\nNew Customer ID: {new_id}")
    name   = input("Full Name    : ")
    email  = input("Email        : ")
    phone  = input("Phone        : ")
    city   = input("City         : ")
    gender = input("Gender (Male/Female): ")
    dob    = input("DOB (YYYY-MM-DD)    : ")
    tier   = input("Tier (Gold/Silver/Bronze): ")

    from datetime import date
    joined = str(date.today())

    new_row = {
        "customer_id" : new_id,
        "name"        : name,
        "email"       : email,
        "phone"       : phone,
        "city"        : city,
        "gender"      : gender,
        "dob"         : dob,
        "joined_date" : joined,
        "tier"        : tier
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    write_csv(df, FILE)
    print(f"Customer {new_id} added successfully!")

def update_customer():
    df = read_csv(FILE)
    cid = input("Enter Customer ID to update: ").strip()

    if cid not in df["customer_id"].values:
        print("Customer not found.")
        return

    print("\nWhat do you want to update?")
    print("1. Email")
    print("2. Phone")
    print("3. City")
    print("4. Tier")
    choice = input("Select: ")

    if choice == "1":
        df.loc[df["customer_id"] == cid, "email"] = input("New Email: ")
    elif choice == "2":
        df.loc[df["customer_id"] == cid, "phone"] = input("New Phone: ")
    elif choice == "3":
        df.loc[df["customer_id"] == cid, "city"]  = input("New City: ")
    elif choice == "4":
        df.loc[df["customer_id"] == cid, "tier"]  = input("New Tier (Gold/Silver/Bronze): ")
    else:
        print("Invalid choice.")
        return

    write_csv(df, FILE)
    print("Customer updated successfully!")

def delete_customer():
    df = read_csv(FILE)
    cid = input("Enter Customer ID to delete: ").strip()

    if cid not in df["customer_id"].values:
        print("Customer not found.")
        return

    confirm = input(f"Are you sure you want to delete {cid}? (yes/no): ")
    if confirm.lower() == "yes":
        df = df[df["customer_id"] != cid]
        write_csv(df, FILE)
        print("Customer deleted successfully!")
    else:
        print("Deletion cancelled.")
