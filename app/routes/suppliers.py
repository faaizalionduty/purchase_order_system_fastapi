from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.supplier import SupplierCreate, SupplierResponse
from app.models.supplier import Supplier
from app.utils.jwt_handler import *

router = APIRouter(prefix="/suppliers", tags=["Suppliers"])

@router.post("/", response_model=SupplierResponse,
             dependencies=[Depends(require_roles("ADMIN"))])
def create_supplier(data: SupplierCreate, db: Session = Depends(get_db)):
    supplier = Supplier(**data.dict())
    db.add(supplier)
    db.commit()
    db.refresh(supplier)
    return supplier
