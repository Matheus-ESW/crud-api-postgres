import datetime
from pydantic import BaseModel, PositiveFloat, EmailStr
from typing import Optional

class ProductBase(BaseModel):
    prod_base_name: str
    prod_base_description: str
    prod_base_price: PositiveFloat
    prod_base_category: str
    prod_base_email_forn: EmailStr

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    prod_base_id: int
    prod_base_created_at: datetime

    class Config:
        from_attributes = True

class ProductUpdate(BaseModel):
    prod_base_name: Optional[str] = None
    prod_base_description: Optional[str] = None
    prod_base_price: Optional[PositiveFloat] = None
    prod_base_category: Optional[str] = None
    prod_base_email_forn: Optional[EmailStr] = None