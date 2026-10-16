# src/sales_api/repositories/customer.py
from sqlalchemy.orm import Session
from sqlalchemy import select

from sales_api.models.customers import Customer

def get_all_customers(
    db: Session,
    limit: int,
    offset: int
):
    stmt = (
        select(Customer)
        .order_by(Customer.customerid)
        .limit(limit)
        .offset(offset)
    )

    result = db.execute(stmt)
    return result.scalars().all()