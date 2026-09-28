import csv

products = [
    {
        "id": 1,
        "name": "Wireless Keyboard Pro",
        "description": "A compact wireless keyboard with a long battery life.",
        "price": 29.99,
        "quantity": 150
    },
    {
        "id": 2,
        "name": "Noise-Cancelling Headphones Max",
        "description": "High-quality headphones with active noise cancellation.",
        "price": 199.99,
        "quantity": 75
    },
    {
        "id": 3,
        "name": "4K Ultra HD Monitor",
        "description": "A stunning 27-inch 4K monitor with vibrant colors.",
        "price": 399.99,
        "quantity": 50
    },
    {
        "id": 4,
        "name": "Bluetooth Speaker",
        "description": "Portable Bluetooth speaker with deep bass and crystal clear sound.",
        "price": 59.99,
        "quantity": 200
    },
    {
        "id": 5,
        "name": "Gaming Mouse Xtreme",
        "description": "Ergonomic gaming mouse with customizable buttons and RGB lighting.",
        "price": 49.99,
        "quantity": 120
    },
    {
        "id": 6,
        "name": "Smartwatch Fit",
        "description": "Fitness-focused smartwatch with heart rate monitor and GPS.",
        "price": 149.99,
        "quantity": 80
    },
    {
        "id": 7,
        "name": "Portable SSD 1TB",
        "description": "High-speed portable SSD with 1TB storage capacity.",
        "price": 129.99,
        "quantity": 90
    },
    {
        "id": 8,
        "name": "USB-C Hub",
        "description": "7-in-1 USB-C hub with HDMI, USB 3.0, and SD card reader.",
        "price": 34.99,
        "quantity": 140
    },
    {
        "id": 9,
        "name": "Mechanical Keyboard",
        "description": "RGB mechanical keyboard with tactile switches.",
        "price": 89.99,
        "quantity": 110
    },
    {
        "id": 10,
        "name": "1080p Webcam",
        "description": "Full HD webcam with built-in microphone for video conferencing.",
        "price": 39.99,
        "quantity": 95
    },
    {
        "id": 1000,
        "name": "Wi-Fi Range Extender",
        "description": "Boost your Wi-Fi signal with this easy-to-install range extender.",
        "price": 49.99,
        "quantity": 130
    }
]



# Define the CSV file path
csv_file_path = "db_products.csv"

# Write the products data to a CSV file
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["id", "name", "description", "price", "quantity"])
    writer.writeheader()  # Write the header row
    writer.writerows(products)  # Write the product data

print(f"Data successfully saved to {csv_file_path}")