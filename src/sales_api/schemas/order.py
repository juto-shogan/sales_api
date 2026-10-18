# src/sales_api/schemas/order.py
from pydantic import BaseModel

from datetime import datetime
from decimal import Decimal

class OrderSummary(BaseModel):
    salesorderid: int
    orderdate: datetime
    status: int
    customerid: int
    onlineorderflag: bool
    totaldue: Decimal | None
    
class OrderRead(OrderSummary):
    duedate: datetime
    shipdate: datetime | None
    subtotal: Decimal
    taxamt: Decimal
    freight: Decimal