from flask import request
from app.schemas.user_schema import UserSchema
from pydantic import ValidationError
from flask_restful import Resource
from app.models.user_model import User
from db import db

class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = UserSchema(**data)
           
            user = User(
                name=validated_data.name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                password=validated_data.password,
            )

            db.session.add(user)
            db.session.commit()

            return {
                'message': 'User registered successfully',
                'data': None
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
