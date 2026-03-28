def add_product(inventory, name, price, quantity):
    """Adds a product dictionary to the inventory list."""
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product)
    print(f"Product '{name}' added successfully.")

def show_inventory(inventory):
    """Displays all products in a simple table format."""
    if not inventory:
        print("The inventory is empty.")
        return
    print("\n--- Current Inventory ---")
    for p in inventory:
        print(f"Name: {p['name']} | Price: {p['price']} | Quantity: {p['quantity']}")

def find_product(inventory, name):
    """Searches for a product by name and returns the dict or None."""
    for p in inventory:
        if p["name"].lower() == name.lower():
            return p
    return None

def update_product(inventory, name, new_price=None, new_quantity=None):
    """Updates the price or quantity of an existing product."""
    p = find_product(inventory, name)
    if p:
        if new_price is not None:
            p["price"] = new_price
        if new_quantity is not None:
            p["quantity"] = new_quantity
        print(f"Product '{name}' updated.")
    else:
        print("Product not found.")

def delete_product(inventory, name):
    """Removes a product from the list by its name."""
    p = find_product(inventory, name)
    if p:
        inventory.remove(p)
        print(f"Product '{name}' deleted.")
    else:
        print("Product not found for deletion.")

def calculate_statistics(inventory):
    """Calculates inventory metrics and returns them in a dictionary."""
    if not inventory:
        return None
    
    # Using lambda to calculate subtotal (price * quantity)
    subtotal = lambda item: item["price"] * item["quantity"]
    
    total_units = sum(p["quantity"] for p in inventory)
    total_value = sum(subtotal(p) for p in inventory)
    
    # Find most expensive product and highest stock
    most_expensive = max(inventory, key=lambda x: x["price"])
    highest_stock = max(inventory, key=lambda x: x["quantity"])
    
    return {
        "units": total_units,
        "value": total_value,
        "expensive": most_expensive,
        "stock": highest_stock
    }