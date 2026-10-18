# src/sales_api/repositories/orders.py
from sqlalchemy.orm import Session
from sqlalchemy import select

from sales_api.models.order import Order

def list_orders(db:Session):
    stmt= select(Order)
    result = db.execute(stmt)
    return result.scalars().all()

def get_order_by_id(db: Session, order_id:int):
    stmt=(
        select(Order)
        .where(Order.salesorderid == order_id)
    )
    result = db.execute(stmt)
    return result.scalar_one_or_none()

