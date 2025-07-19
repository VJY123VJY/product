from pydantic import BaseModel
from typing import Optional
from enum import Enum


class CategoryEnum(str, Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"


class UnitEnum(str, Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"


class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: UnitEnum
    lead_time: int


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductOut(ProductBase):
    id: int

    class Config:
        from_attributes = True
