import csv

def save_csv(inventory, path):
    """Saves the inventory list to a CSV file."""
    if not inventory:
        print("Error: Inventory is empty.")
        return
    try:
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            writer.writerows(inventory)
        print(f"Inventory saved in: {path}")
    except Exception as e:
        print(f"Error while saving: {e}")

def load_csv(path):
    """Reads a CSV and returns a validated list of products."""
    products = []
    errors = 0
    try:
        with open(path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    name = row["name"].strip()
                    # VALIDATION: Letters only and not empty
                    if not name or not name.isalpha():
                        errors += 1
                        continue
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    if price < 0 or quantity < 0:
                        errors += 1
                        continue
                    products.append({"name": name, "price": price, "quantity": quantity})
                except:
                    errors += 1
        return products, errors
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None, errors