from pydantic import BaseModel

class SupplierCreate(BaseModel):
    name: str
    contact_email: str
    phone: str

class SupplierResponse(SupplierCreate):
    id: int

    class Config:
        from_attributes = True
