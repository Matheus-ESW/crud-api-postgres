from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from backend.conn.connDatabase import Base

class ProductModel(Base):
    __tablename__ = "products"

    prod_base_id = Column(Integer, primary_key=True)
    prod_base_name = Column(String)
    prod_base_description = Column(String)
    prod_base_price = Column(Float)
    prod_base_category = Column(String)
    prod_base_email_forn = Column(String)
    prod_base_created_at = Column(DateTime(timezone=True), default=func.now())