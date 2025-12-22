from fastapi import FastAPI
from app.routes import users, suppliers, products, purchase_orders
from app.database import *

Base.metadata.create_all(bind = engine)

app = FastAPI(title="Purchase Order Management System")

app.include_router(users.router)
app.include_router(suppliers.router)
app.include_router(products.router)
app.include_router(purchase_orders.router)
