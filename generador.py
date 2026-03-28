import csv
def create_initial_file():
    path = "inventory.csv"
    data = [
        {"name": "Apple", "price": 1.5, "quantity": 100},
        {"name": "Bread", "price": 2.1, "quantity": 50},
        {"name": "Milk", "price": 1.2, "quantity": 30}
    ]
    try:
        with open(path, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            writer.writerows(data)
        print(f"Success: '{path}' created.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_initial_file()