from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class Customer(db.Model):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    document_number = Column(String(8), nullable=False, unique=True)
    address = Column(String(255), nullable=False)