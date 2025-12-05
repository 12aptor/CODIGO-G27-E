from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class Product(db.Model):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)