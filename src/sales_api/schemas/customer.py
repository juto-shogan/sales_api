# src/sales_api/schemas/customer.py
from pydantic import BaseModel

class CustomerRead(BaseModel):
    customerid: int
    personid: int | None = None
    storeid: int | None = None
    territoryid: int | None = None