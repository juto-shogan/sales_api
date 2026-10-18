# src/sales_api/models/order.py
from sqlalchemy.orm import Mapped, mapped_column

from datetime import datetime
from decimal import Decimal

from sales_api.models.base import Base

class Order(Base):
    __tablename__ = "salesorderheader"
    __table_args__ = {"schema": "sales"}
    
    salesorderid: Mapped[int] = mapped_column(primary_key=True)
    orderdate: Mapped[datetime]
    duedate: Mapped[datetime]
    shipdate: Mapped[datetime | None]
    status: Mapped[int]
    onlineorderflag: Mapped[bool]
    customerid: Mapped[int]
    subtotal: Mapped[Decimal]
    taxamt: Mapped[Decimal]
    freight: Mapped[Decimal]
    totaldue: Mapped[Decimal | None]
