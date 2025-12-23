from pydantic import BaseModel
from typing import List
from datetime import datetime

class PurchaseItemCreate(BaseModel):
    product_id: int
    quantity: int
    price: float

class PurchaseItemResponse(PurchaseItemCreate):
    id: int

    class Config:
        from_attributes = True

class PurchaseOrderCreate(BaseModel):
    supplier_id: int
    items: List[PurchaseItemCreate]

class PurchaseOrderResponse(BaseModel):
    id: int
    supplier_id: int
    status: str
    created_at: datetime
    items: List[PurchaseItemResponse]
    total: float

    class Config:
        from_attributes = True
