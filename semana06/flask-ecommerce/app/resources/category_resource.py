from flask import request
from flask_restful import Resource
from pydantic import ValidationError
from app.schemas.category_schema import CategorySchema
from app.models.category_model import Category
from db import db

class CategoyResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = CategorySchema(**data)

            category = Category(name=validated_data.name)

            db.session.add(category)
            db.session.commit()

            return {
                'message': 'Category created successfully',
                'data': {
                    'id': category.id,
                    'name': category.name,
                    'status': category.status
                }
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def get(self):
        try:
            categories = Category.query.filter_by(status=True)

            response = []
            for category in categories:
                category_dict = {
                    'id': category.id,
                    'name': category.name,
                    'status': category.status
                }
                response.append(category_dict)

            return {
                'message': 'Categories fetched successfully',
                'data': response
            },200
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
class ManageCategoryResource(Resource):
    def get(self, id):
        try:
            category = Category.query.get(id)

            if not category:
                return {
                    'error': 'Category not found'
                }, 404

            return {
                'message': 'Category fetched successfully',
                'data': {
                    'id': category.id,
                    'name': category.name,
                    'status': category.status
                }
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def put(self, id):
        try:
            data = request.get_json()
            validated_data = CategorySchema(**data)

            category = Category.query.get(id)

            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            category.name = validated_data.name

            db.session.commit()

            return {
                'message': 'Category updated successfully',
                'data': {
                    'id': category.id,
                    'name': category.name,
                    'status': category.status
                }
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def delete(self, id):
        try:
            category = Category.query.get(id)

            if not category:
                return {
                    'error': 'Category not found'
                }, 404
            
            category.status = False

            db.session.commit()

            return {
                'message': 'Category deleted successfully'
            }, 200
        except Exception as e:
            return {
                'error': str(e)
            }, 400