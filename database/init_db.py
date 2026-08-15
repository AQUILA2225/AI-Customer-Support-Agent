import sqlite3


def create_database():
    connection = sqlite3.connect("orders.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_name TEXT NOT NULL,
            product_name TEXT NOT NULL,
            status TEXT NOT NULL,
            estimated_delivery TEXT
        )
    """)

    sample_orders = [
        (
            "ORD1001",
            "Aquila",
            "Wireless Headphones",
            "Shipped",
            "2026-08-15"
        ),
        (
            "ORD1002",
            "John",
            "Mechanical Keyboard",
            "Processing",
            "2026-08-18"
        ),
        (
            "ORD1003",
            "Sarah",
            "Smart Watch",
            "Out for Delivery",
            "2026-08-13"
        ),
        (
            "ORD1004",
            "David",
            "Laptop Stand",
            "Delivered",
            "2026-08-10"
        )
    ]

    cursor.executemany("""
        INSERT OR REPLACE INTO orders
        (order_id, customer_name, product_name, status, estimated_delivery)
        VALUES (?, ?, ?, ?, ?)
    """, sample_orders)

    connection.commit()
    connection.close()

    print("Database created successfully!")


if __name__ == "__main__":
    create_database()