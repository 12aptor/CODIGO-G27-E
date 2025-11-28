from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
)

class Role(db.Model):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False, unique=True)