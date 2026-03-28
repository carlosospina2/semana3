import services
import files

def menu():
    memory_inventory = []
    file_path = "inventory.csv"
    running = True

    while running:
        print("\n--- INVENTORY SYSTEM ---")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Search product")
        print("4. Update product")
        print("5. Delete product")
        print("6. View statistics")
        print("7. Save to CSV")
        print("8. Load from CSV")
        print("9. Exit")
        
        option = input("Select an option (1-9): ")

        if option == "1":
            try:
                name = input("Name: ").strip()
                if not name or not name.isalpha():
                    print("Error: Invalid name (letters only).")
                else:
                    price = float(input("Price: "))
                    quantity = int(input("Quantity: "))
                    if price < 0 or quantity < 0:
                        print("Error: No negative values.")
                    else:
                        services.add_product(memory_inventory, name, price, quantity)
            except ValueError:
                print("Error: Please enter valid numbers.")
        
        elif option == "2":
            services.show_inventory(memory_inventory)

        elif option == "3":
            name = input("Name to search for: ")
            p = services.find_product(memory_inventory, name)
            if p:
                print(f"Found: {p}")
            else:
                print("Product not found.")

        elif option == "4":
            name = input("Product name to update: ")
            try:
                price_input = input("New price (leave empty to keep current): ")
                qty_input = input("New quantity (leave empty to keep current): ")
                
                new_p = float(price_input) if price_input else None
                new_q = int(qty_input) if qty_input else None
                
                services.update_product(memory_inventory, name, new_p, new_q)
            except ValueError:
                print("Error: Please enter valid numeric values.")

        elif option == "5":
            name = input("Product name to delete: ")
            services.delete_product(memory_inventory, name)

        elif option == "6":
            stats = services.calculate_statistics(memory_inventory)
            if stats:
                print(f"\n--- STATISTICS ---")
                print(f"Total units: {stats['units']}")
                print(f"Total business value: ${stats['value']:.2f}")
                print(f"Most expensive: {stats['expensive']['name']} (${stats['expensive']['price']})")
                print(f"Highest stock: {stats['stock']['name']} ({stats['stock']['quantity']} units)")
            else:
                print("No data available for statistics.")

        elif option == "7":
            files.save_csv(memory_inventory, file_path)

        elif option == "8":
            data, error_rows = files.load_csv(file_path)
            if data is not None:
                decision = input("Overwrite current inventory? (Y/N): ").upper()
                if decision == "Y":
                    memory_inventory = data
                    print("Inventory replaced.")
                else:
                    # Merge policy: Sum quantity and update price
                    for new_p in data:
                        existing_p = services.find_product(memory_inventory, new_p["name"])
                        if existing_p:
                            existing_p["quantity"] += new_p["quantity"]
                            existing_p["price"] = new_p["price"]
                        else:
                            memory_inventory.append(new_p)
                    print("Inventory merged.")
                
                print(f"Summary: {len(data)} loaded, {error_rows} invalid rows skipped.")

        elif option == "9":
            print("Exiting program...")
            running = False
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    menu()