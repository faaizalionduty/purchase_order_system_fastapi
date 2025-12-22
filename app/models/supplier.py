from sqlalchemy import Column, Integer, String
from app.database import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    contact_email = Column(String)
    phone = Column(String)
