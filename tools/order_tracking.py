import sqlite3
from langchain_core.tools import tool


@tool
def get_order_status(order_id: str) -> dict:
    """
    Get the current status and estimated delivery date for a customer order.

    Use this tool when a customer asks about:
    - Order status
    - Order tracking
    - Shipping status
    - Estimated delivery date

    The customer must provide an order ID, for example ORD1001.
    """

    connection = sqlite3.connect("database/orders.db")
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT order_id, customer_name, product_name,
        status, estimated_delivery
        FROM orders
        WHERE order_id = ?
        """,
        (order_id,)
    )

    order = cursor.fetchone()

    connection.close()

    if order is None:
        return {
            "found": False,
            "message": f"No order found with ID {order_id}"
        }

    return {
        "found": True,
        "order_id": order[0],
        "customer_name": order[1],
        "product_name": order[2],
        "status": order[3],
        "estimated_delivery": order[4]
    }


if __name__ == "__main__":
    result = get_order_status.invoke(
        {"order_id": "ORD1001"}
    )

    print(result)