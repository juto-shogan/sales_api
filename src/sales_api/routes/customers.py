from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from sales_api.database import get_db
from sales_api.schemas.customers import Customer
from sales_api.repositories import customers as customer_repo

router = APIRouter()

@router.get("/customers", response_model=list[Customer])
def get_all_customers(
    db: Session = Depends(get_db),
    limit: int = Query(default = 1000, ge=1, le=100),
    offset: int = Query(default=0, ge=0)
):
    return customer_repo.get_all_customers(db, limit, offset)