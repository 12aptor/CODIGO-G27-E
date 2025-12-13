from pydantic import BaseModel

class CustomerSchema(BaseModel):
    name: str
    last_name: str
    email: str
    document_number: str
    address: str

class SaleDetailSchema(BaseModel):
    quantity: int
    price: float
    subtotal: float
    product_id: int

class SaleSchema(BaseModel):
    total: float
    customer: CustomerSchema
    sale_details: list[SaleDetailSchema]