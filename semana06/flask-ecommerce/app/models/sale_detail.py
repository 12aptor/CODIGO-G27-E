from db import db
from sqlalchemy import (
    Column,
    Integer,
    Float,
    ForeignKey,
)

class SaleDetail(db.Model):
    __tablename__ = 'sale_details'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    sale_id = Column(Integer, ForeignKey('sales.id'), nullable=False)