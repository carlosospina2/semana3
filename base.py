import csv

def generate_initial_file(path):
    """Creates a sample CSV file with test data in English."""
    # Test data following the format: name, price, quantity
    initial_data = [
        {"name": "Apple", "price": 1.5, "quantity": 100},
        {"name": "Bread", "price": 2.1, "quantity": 50},
        {"name": "Milk", "price": 1.2, "quantity": 30}
    ]
    
    try:
        with open(path, mode='w', newline='', encoding='utf-8') as file:
            # Defined the exact headers required by your instructions
            columns = ["name", "price", "quantity"]
            writer = csv.DictWriter(file, fieldnames=columns)
            
            writer.writeheader() # Writes: name,price,quantity
            writer.writerows(initial_data)
            
        print(f"File '{path}' successfully created with {len(initial_data)} products.")
    except Exception as e:
        print(f"Could not create the file: {e}")

# Run the function
if __name__ == "__main__":
    generate_initial_file("inventory.csv")