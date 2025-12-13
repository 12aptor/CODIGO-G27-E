from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.product_schema import ProductSchema
from app.models.product_model import Product
from db import db
from app.utils.helpers import CloudinaryHelper

cloudinary_helper = CloudinaryHelper()

class ProductResource(Resource):
    def post(self):
        try:
            data = request.form
            validated_data = ProductSchema(**data)

            image = request.files.get('image')

            if not image:
                return {
                    'error': 'Image is required'
                }, 400

            if image.filename == '':
                return {
                    'error': 'Image is required'
                }, 400
            
            if not image.content_type.startswith('image/'):
                return {
                    'error': 'Invalid image type'
                }, 400
                
            secure_url, public_id = cloudinary_helper.upload_image(image, 'products')

            if not secure_url:
                return {
                    'error': 'Error uploading image'
                }, 400

            product = Product(
                name=validated_data.name,
                description=validated_data.description,
                image=public_id,
                brand=validated_data.brand,
                size=validated_data.size,
                price=validated_data.price,
                stock=validated_data.stock,
                category_id=validated_data.category_id
            )

            db.session.add(product)
            db.session.commit()

            return {
                'message': 'Product created successfully',
                'data': {
                    'id': product.id,
                    'code': f'P-{str(product.id).zfill(4)}',
                    'name': product.name,
                    'description': product.description,
                    'image': secure_url,
                    'brand': product.brand,
                    'size': product.size,
                    'price': product.price,
                    'stock': product.stock,
                    'status': product.status,
                    'category_id': product.category_id
                }
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            },400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def get(self):
        try:
            products = Product.query.filter_by(status=True)

            response = []
            for product in products:
                product_dict = {
                    'id': product.id,
                    'code': f'P-{str(product.id).zfill(4)}',
                    'name': product.name,
                    'description': product.description,
                    'image': cloudinary_helper.get_secure_url(product.image),
                    'brand': product.brand,
                    'size': product.size,
                    'price': product.price,
                    'stock': product.stock,
                    'status': product.status,
                    'category': {
                        'id': product.category.id,
                        'name': product.category.name,
                        'status': product.category.status
                    }
                }
                response.append(product_dict)

            return {
                'message': 'Products fetched successfully',
                'data': response
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400