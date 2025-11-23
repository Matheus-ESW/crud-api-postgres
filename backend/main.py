from fastapi import FastAPI
from backend.conn.connDatabase import engine
from backend.models import productModel
from backend.routers.productRouters import prod_router

productModel.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(prod_router)