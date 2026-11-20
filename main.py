from modules import products, customers, orders, reports

def product_menu():
    while True:
        print("\n--- Products ---")
        print("1. View All Products")
        print("2. Search Product")
        print("3. Add Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("0. Back")
        choice = input("Select: ")
        if   choice == "1": products.view_products()
        elif choice == "2": products.search_product()
        elif choice == "3": products.add_product()
        elif choice == "4": products.update_product()
        elif choice == "5": products.delete_product()
        elif choice == "0": break
        else: print("Invalid choice.")

def customer_menu():
    while True:
        print("\n--- Customers ---")
        print("1. View All Customers")
        print("2. Search Customer")
        print("3. Add Customer")
        print("4. Update Customer")
        print("5. Delete Customer")
        print("0. Back")
        choice = input("Select: ")
        if   choice == "1": customers.view_customers()
        elif choice == "2": customers.search_customer()
        elif choice == "3": customers.add_customer()
        elif choice == "4": customers.update_customer()
        elif choice == "5": customers.delete_customer()
        elif choice == "0": break
        else: print("Invalid choice.")

def order_menu():
    while True:
        print("\n--- Orders ---")
        print("1. View All Orders")
        print("2. View Order Details")
        print("3. Place Order")
        print("4. Update Order Status")
        print("5. Cancel Order")
        print("0. Back")
        choice = input("Select: ")
        if   choice == "1": orders.view_orders()
        elif choice == "2": orders.view_order_details()
        elif choice == "3": orders.place_order()
        elif choice == "4": orders.update_status()
        elif choice == "5": orders.cancel_order()
        elif choice == "0": break
        else: print("Invalid choice.")

def reports_menu():
    while True:
        print("\n--- Reports ---")
        print("1. Sales Summary")
        print("2. Top Selling Products")
        print("3. Low Stock Alert")
        print("4. Orders by Status")
        print("5. Revenue by Category")
        print("6. Export Report")
        print("0. Back")
        choice = input("Select: ")
        if   choice == "1": reports.sales_summary()
        elif choice == "2": reports.top_products()
        elif choice == "3": reports.low_stock_alert()
        elif choice == "4": reports.orders_by_status()
        elif choice == "5": reports.revenue_by_category()
        elif choice == "6": reports.export_report()
        elif choice == "0": break
        else: print("Invalid choice.")

def main_menu():
    while True:
        print("\n===== E-COMMERCE DASHBOARD =====")
        print("1. Products")
        print("2. Customers")
        print("3. Orders")
        print("4. Reports")
        print("0. Exit")
        choice = input("Select: ")
        if   choice == "1": product_menu()
        elif choice == "2": customer_menu()
        elif choice == "3": order_menu()
        elif choice == "4": reports_menu()
        elif choice == "0":
            print("Goodbye!")
            break
        else: print("Invalid choice.")

main_menu()
