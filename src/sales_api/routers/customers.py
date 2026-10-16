# /src/sales_api/routers
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from sales_api.database import get_db
from sales_api.schemas.customer import CustomerRead
from sales_api.repositories import customers as customer_repo

router = APIRouter(prefix="/customers", tags=["customers"])

@router.get("", response_model=list[CustomerRead])
def get_customers(
    db: Session = Depends(get_db),
    limit: int = Query(default = 50, ge=1, le=100),
    offset: int = Query(default=0, ge=0)
):
    return customer_repo.get_all_customers(db, limit, offset)


@router.get("/{customer_id}", response_model=CustomerRead)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = customer_repo.get_specific_customer(db, customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer