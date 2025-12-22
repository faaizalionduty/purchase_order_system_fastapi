from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.purchase_order import PurchaseOrderCreate, PurchaseOrderResponse
from app.models.purchase_order import PurchaseOrder
from app.models.purchase_item import PurchaseItem
from app.utils.jwt_handler import require_roles

router = APIRouter(prefix="/purchase-orders", tags=["Purchase Orders"])

@router.post("/", response_model=PurchaseOrderResponse,
             dependencies=[Depends(require_roles("PROCUREMENT"))])
def create_po(data: PurchaseOrderCreate, db: Session = Depends(get_db)):
    po = PurchaseOrder(supplier_id=data.supplier_id)
    db.add(po)
    db.commit()
    db.refresh(po)

    for item in data.items:
        db.add(PurchaseItem(order_id=po.id, **item.dict()))
    db.commit()
    db.refresh(po)
    return po

@router.put("/{po_id}/approve",
            dependencies=[Depends(require_roles("FINANCE"))])
def approve_po(po_id: int, db: Session = Depends(get_db)):
    po = db.query(PurchaseOrder).get(po_id)
    if not po:
        raise HTTPException(404, "PO not found")
    po.status = "APPROVED"
    db.commit()
    return {"message": "Approved"}

@router.put("/{po_id}/receive",
            dependencies=[Depends(require_roles("WAREHOUSE"))])
def receive_po(po_id: int, db: Session = Depends(get_db)):
    po = db.query(PurchaseOrder).get(po_id)
    if not po:
        raise HTTPException(404, "PO not found")
    po.status = "RECEIVED"
    db.commit()
    return {"message": "Goods received"}
