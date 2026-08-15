from pydantic import BaseModel
from typing import Optional


class OrderResponse(BaseModel):
    found: bool
    order_id: Optional[str] = None
    customer_name: Optional[str] = None
    product_name: Optional[str] = None
    status: Optional[str] = None
    estimated_delivery: Optional[str] = None
    message: Optional[str] = None