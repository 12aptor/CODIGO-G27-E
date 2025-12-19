from flask import request
from flask_restful import Resource
from app.schemas.sale_schema import SaleSchema
from pydantic import ValidationError
from app.models.product_model import Product
from app.models.sale_detail_model import SaleDetail
from app.models.customer_model import Customer
from app.models.sale_model import Sale
from db import db

class SaleResource(Resource):
    def get(self):
        try:
            sales = Sale.query.all()

            response = []
            for sale in sales:
                sale_details = []
                for detail in sale.sale_details:
                    detail_dict = {
                        'id': detail.id,
                        'quantity': detail.quantity,
                        'subtotal': detail.subtotal,
                        'product': {
                            'id': detail.product.id,
                            'name': detail.product.name,
                            'description': detail.product.description
                        },
                    }
                    sale_details.append(detail_dict)

                sale_dict = {
                    'id': sale.id,
                    'code': sale.code,
                    'total': sale.total,
                    'status': sale.status.value,
                    'created_at': str(sale.created_at),
                    'customer': {
                        'id': sale.customer.id,
                        'name': sale.customer.name,
                        'last_name': sale.customer.last_name,
                        'email': sale.customer.email,
                        'document_number': sale.customer.document_number,
                        'address': sale.customer.address
                    },
                    'sale_details': sale_details
                }
                response.append(sale_dict)

            return {
                'message': 'Sales fetched successfully',
                'data': response
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400

    def post(self):
        try:
            data = request.get_json()
            validated_data = SaleSchema(**data)

            sale_details = []
            for new_sale_detail in validated_data.sale_details:
                product = Product.query.get(new_sale_detail.product_id)

                if not product:
                    return {
                        'error': 'Product not found'
                    }, 404
                
                if product.status == False:
                    return {
                        'error': 'Product is out of stock'
                    }, 404
                
                if product.stock < new_sale_detail.quantity:
                    return {
                        'error': 'Not enough stock'
                    }, 400
                
                product.stock -= new_sale_detail.quantity

                new_sale_detail = SaleDetail(
                    quantity=new_sale_detail.quantity,
                    price=new_sale_detail.price,
                    subtotal=new_sale_detail.subtotal,
                    product_id=new_sale_detail.product_id
                )
                sale_details.append(new_sale_detail)

            customer = Customer.query.filter_by(
                document_number=validated_data.customer.document_number
            ).first()

            if not customer:
                customer = Customer(
                    name=validated_data.customer.name,
                    last_name=validated_data.customer.last_name,
                    email=validated_data.customer.email,
                    document_number=validated_data.customer.document_number,
                    address=validated_data.customer.address
                )
                db.session.add(customer)
            else:
                customer.name = validated_data.customer.name
                customer.last_name = validated_data.customer.last_name
                customer.email = validated_data.customer.email
                customer.document_number = validated_data.customer.document_number
                customer.address = validated_data.customer.address

            db.session.flush()

            last_sale = Sale.query.order_by(
                Sale.id.desc()
            ).first()
            sale_code = 'B-0001'
            if last_sale:
                last_code = last_sale.code
                last_number = int(last_code.split('-')[1])
                new_number = last_number + 1
                sale_code = f'B-{str(new_number).zfill(4)}'

            sale = Sale(
                code=sale_code,
                total=validated_data.total,
                customer_id=customer.id,
                sale_details=sale_details
            )

            db.session.add(sale)
            db.session.commit()

            return {
                'message': 'Sale created successfully',
                'data': {
                    'id': sale.id,
                    'code': sale.code,
                    'total': sale.total
                }
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            db.session.rollback()
            return {
                'error': str(e)
            }, 400