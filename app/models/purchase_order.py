from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    status = Column(String, default="PENDING")
    created_at = Column(DateTime, default=datetime.utcnow)

    supplier = relationship("Supplier")
    items = relationship("PurchaseItem", back_populates="order")
