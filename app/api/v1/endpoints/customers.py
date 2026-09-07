from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.crud.customer import create_customer, get_customer_by_id
from app.schemas.customer import CustomerCreate, CustomerResponse

router = APIRouter()


@router.post("/customers", response_model=CustomerResponse)
def create_new_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):
    return create_customer(db, customer)


@router.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):
    customer = get_customer_by_id(db, customer_id)

    if not customer:
        return {"message": "Customer not found"}

    return customer