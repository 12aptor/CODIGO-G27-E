from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    ForeignKey,
)

class UpdateProductLog(db.Model):
    __tablename__ = 'update_product_logs'

    id = Column(Integer, primary_key=True)
    field = Column(String(100), nullable=False)
    value = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)