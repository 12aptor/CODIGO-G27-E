from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
)

class Category(db.Model):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    status = Column(Boolean, default=True)