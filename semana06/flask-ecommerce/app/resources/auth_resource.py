from flask import request
from app.models.user_model import User
from db import db
from app.schemas.auth_schema import (
    RegisterSchema,
    LoginSchema,
)
import bcrypt
from pydantic import ValidationError
from flask_restful import Resource
from app.utils.helpers import CryptoHelper
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
)

class RegisterResource(Resource):
    def post(self):
        try:
            data = request.get_json()
            validated_data = RegisterSchema(**data)

            existing_user = User.query.filter_by(
                email=validated_data.email
            ).first()

            if existing_user:
                return {
                    'error': 'User already exists'
                }, 400
            
            user = User(
                name=validated_data.name,
                last_name=validated_data.last_name,
                email=validated_data.email,
                password=self.__hash_password(validated_data.password),
                role_id=validated_data.role_id
            )

            db.session.add(user)
            db.session.commit()

            return {
                'message': 'User created successfully',
                'data': {
                    'id': user.id,
                    'name': user.name,
                    'last_name': user.last_name,
                    'email': user.email,
                    'role_id': user.role_id
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

    def __hash_password(self, password: str) -> str:
        bytes_password = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(bytes_password, bcrypt.gensalt())
        return hashed_password.decode('utf-8')

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
            
            password_verified = self.__verify_password(
                user.password,
                validated_data.password
            )

            if password_verified == False:
                return {
                    'error': 'Email or password is incorrect'
                }, 401
            
            cryptop_helper = CryptoHelper()
            hashed_id = cryptop_helper.encrypt(user.id)

            access_token = create_access_token(
                identity=hashed_id,
                additional_claims={
                    'name': user.name,
                    'last_name': user.last_name,
                    'email': user.email,
                }
            )
            refresh_token = create_refresh_token(identity=hashed_id)

            return {
                'access_token': access_token,
                'refresh_token': refresh_token,
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
        bytes_hashed_password = hashed_password.encode('utf-8')
        bytes_password = password.encode('utf-8')
        return bcrypt.checkpw(bytes_password, bytes_hashed_password)