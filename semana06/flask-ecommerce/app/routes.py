from flask_restful import Api
from app import app
from app.resources.auth_resource import (
    RegisterResource,
    LoginResource,
)
from app.resources.category_resource import (
    CategoyResource,
    ManageCategoryResource,
)

api = Api(app, prefix='/api/v1')

api.add_resource(RegisterResource, '/auth/register')
api.add_resource(LoginResource, '/auth/login')

api.add_resource(CategoyResource, '/categories')
api.add_resource(ManageCategoryResource, '/categories/<int:id>')