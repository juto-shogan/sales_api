# src/sales_api/schemas/customer.py
from pydantic import BaseModel, ConfigDict

class Customer(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    customerid: int
    personid: int | None = None
    storeid: int | None = None
    territoryid: int | None = None

