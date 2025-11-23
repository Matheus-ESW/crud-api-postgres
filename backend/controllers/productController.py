from sqlalchemy.orm import Session
from views.productView import ProductCreate, ProductUpdate
from models.productModel import ProductModel

def get_all_products(db: Session):
    """
    Essa função retorna todos os produtos pertencentes a tabela Products.
    """
    return db.query(ProductModel).all()

def get_product(db: Session, product_id: int):
    """
    Essa função retorna um produto pertencente a tabela Products, filtrando pelo ID.
    """
    return db.query(ProductModel).filter(ProductModel.prod_base_id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    """
    Essa função insere um produto na tabela Products.
    """
    db_product = ProductModel(**product.model_dump())
    db_product.add(db_product)
    db.commit()
    db.refresh(db_product)
    
    return db_product

def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Essa função atualiza algum atributo de um produto da tabela Products, filtrando pelo ID.
    """
    db_product = db.query(ProductModel).filter(ProductModel.prod_base_id == product_id).first()

    if db_product is None:
        return None
    
    if product.prod_base_name is not None:
        db_product.prod_base_name = product.prod_base_name
    if product.prod_base_description is not None:
        db_product.prod_base_description = product.prod_base_description
    if product.prod_base_price is not None:
        db_product.prod_base_price = product.prod_base_price
    if product.prod_base_category is not None:
        db_product.prod_base_category = product.prod_base_category
    if product.prod_base_email_forn is not None:
        db_product.prod_base_email_forn = product.prod_base_email_forn

    db.commit
    return db_product

def delete_product(db: Session, product_id: int):
    """
    Essa função remove algum produto da tabela Products, filtrando pelo ID.
    """
    db_product = db.query(ProductModel).filter(ProductModel.prod_base_id == product_id).first()
    db.delete(db_product)
    db.commit()

    return db_product