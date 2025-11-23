from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from conn.connDatabase import get_db
from views.productView import ProductResponse, ProductCreate, ProductUpdate
from controllers.productController import get_all_products, get_product, create_product, update_product, delete_product

prod_router = APIRouter()

@prod_router.get("/products/", response_model=List[ProductResponse])
def get_all_products_route(db: Session = Depends(get_db)):
    """
    Essa é a rota que retorna todos os produtos do banco de dados, pertencentes a tabela Products.
    """
    products = get_all_products(db)

    return products

@prod_router.get("/products/{product_id}", response_model=ProductResponse)
def get_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Essa é a rota que retorna um produto do banco de dados, pertencente a tabela Products, filtrado pelo ID.
    """
    db_product = get_product(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado!!")
    
    return db_product

@prod_router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Essa é a rota que insere um produto do banco de dados, pertencente a tabela Products.
    """
    return create_product(db=db, product=product)

@prod_router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """
    Essa é a rota que atualiza algum atributo de algum produto do banco de dados, pertencente a tabela Products, filtrado pelo ID.
    """
    db_product = update_product(db, product_id=product_id, product=product)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado!!")
    
    return db_product

@prod_router.delete("/products/{product_id}", response_model=ProductResponse)
def detele_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Essa é a rota que deleta um produto do banco de dados, pertencente a tabela Products, filtrado pelo ID.
    """
    db_product = delete_product(db, product_id=product_id)

    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    
    return db_product