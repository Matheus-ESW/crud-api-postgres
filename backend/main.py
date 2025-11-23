from fastapi import FastAPI
from conn.connDatabase import engine
from models import productModel
from routers.productRouters import prod_router

productModel.Base.metadata.create_all(bind=engine)

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Criando primeira API com FastAPI e usando rotas/modular!! API criada pelo Matheus."}
app.include_router(prod_router)