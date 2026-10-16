# src/sales_api/models/customer.py
from sqlalchemy.orm import Mapped, mapped_column

from sales_api.models.base import Base

class Customer(Base):
    __tablename__ = "customer"
    __table_args__ = {"schema": "sales"}
    
    customerid: Mapped[int] = mapped_column(primary_key=True)
    personid: Mapped[int | None]
    storeid: Mapped[int | None]
    territoryid: Mapped[int | None]