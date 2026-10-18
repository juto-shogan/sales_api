# src/sales_Api/routers/order.py
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from sales_api.database import get_db
from sales_api.repositories import orders as ord_repo
from sales_api.schemas.order import (
    OrderSummary,
    OrderRead
)

router = APIRouter(prefix="/orders", tags=["orders"])

@router.get("", response_model=list[OrderSummary])
def get_orders(
    limit: int = Query(default= 10, ge=0, le=100),
    offset: int =  Query(defualt=0, ge=0),
    db: Session= Depends(get_db)
):
    return ord_repo.list_orders(db, limit, offset)

@router.get("/{order_id}", response_model=OrderRead)
def get_order(order_id: int, db: Session=Depends(get_db)):
    order = ord_repo.get_order_by_id(db, order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

