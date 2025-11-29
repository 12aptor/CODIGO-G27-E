from flask import request
from app.schemas.user_schema import UserSchema, LoginSchema
from pydantic import ValidationError
from flask_restful import Resource
from app.models.user_model import User
from db import db
import bcrypt
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)
from app.utils.helpers import CryptoHelper

class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = UserSchema(**data)
           
            user = User(
                name=validated_data.name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                password=self.__hash_password(validated_data.password),
                role_id=validated_data.role_id
            )

            db.session.add(user)
            db.session.commit()

            response = {
                'id': user.id,
                'name': user.name,
                'last_name': user.last_name,
                'email': user.email,
                'role_id': user.role_id
            }

            return {
                'message': 'User registered successfully',
                'data': response
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def __hash_password(self, password: str) -> str:
        bytes_pwd = password.encode('utf-8')
        hash_pwd = bcrypt.hashpw(bytes_pwd, bcrypt.gensalt())
        return hash_pwd.decode('utf-8')
        
class LoginResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = LoginSchema(**data)

            user = User.query.filter_by(
                email=validated_data.email
            ).first()

            if not user:
                return {
                    'error': 'Email or password is incorrect'
                }, 401
            
            pwd_verified = self.__verify_password(
                user.password,
                validated_data.password
            )

            if not pwd_verified:
                return {
                    'error': 'Email or password is incorrect'
                }, 401
            
            crypto_helper = CryptoHelper()
            hashed_id = crypto_helper.encrypt(user.id)

            access_token = create_access_token(identity=hashed_id)
            refresh_token = create_refresh_token(identity=hashed_id)

            response = {
                'access_token': access_token,
                'refresh_token': refresh_token,
            }

            return {
                'message': 'User logged in successfully',
                'data': response
            }, 200
        except ValidationError as e:
            return {
                'error': e.errors()
            }, 400
        except Exception as e:
            return {
                'error': str(e)
            }, 400
        
    def __verify_password(self, hashed_password: str, password: str) -> bool:
        bytes_hashed_pwd = hashed_password.encode('utf-8')
        bytes_pwd = password.encode('utf-8')
        return bcrypt.checkpw(bytes_pwd, bytes_hashed_pwd)