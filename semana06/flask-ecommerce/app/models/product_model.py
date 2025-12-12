from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Float,
    Boolean,
    ForeignKey,
)
from sqlalchemy.orm import relationship

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(255), nullable=False)
    image = Column(Text, nullable=False)
    brand = Column(String(50), nullable=False)
    size = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    status = Column(Boolean, default=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

    category = relationship('Category')