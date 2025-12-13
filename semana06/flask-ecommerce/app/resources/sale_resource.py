from flask import request
from flask_restful import Resource
from app.schemas.sale_schema import SaleSchema
from pydantic import ValidationError
from app.models.product_model import Product

class SaleResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = SaleSchema(**data)

            for sale_detail in validated_data.sale_details:
                product = Product.query.get(sale_detail.product_id)

                if not product:
                    return {
                        'error': 'Product not found'
                    }, 404
                
                if product.stock < sale_detail.quantity:
                    return {
                        'error': 'Not enough stock'
                    }, 400
                
                product.stock -= sale_detail.quantity

            # Validar el stock de los productos

            # Crear la venta

            # Descontar el stock de los productos

            # Generar la factura

            # Finalizar la transacción
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            # Rollback de las transacciones
            return {
                'error': str(e)
            }, 400