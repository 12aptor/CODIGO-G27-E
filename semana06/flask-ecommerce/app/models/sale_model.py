from db import db
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Enum as SqlEnum,
    DateTime,
    func,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from enum import Enum

class SaleStatus(Enum):
    PENDING = 'PENDING'
    COMPLETED = 'COMPLETED'
    CANCELLED = 'CANCELLED'

class Sale(db.Model):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), nullable=False, unique=True)
    total = Column(Float, nullable=False)
    status = Column(SqlEnum(SaleStatus), default=SaleStatus.PENDING)
    created_at = Column(DateTime, default=func.now())
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)

    sale_details = relationship('SaleDetail')