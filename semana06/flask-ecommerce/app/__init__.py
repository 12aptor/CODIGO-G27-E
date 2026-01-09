from flask import Flask
from db import db
from flask_migrate import Migrate
from config import Config
from flask_jwt_extended import JWTManager
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)
cors = CORS(app)

from app.models.category_model import Category
from app.models.customer_model import Customer
from app.models.product_model import Product
from app.models.role_model import Role
from app.models.sale_detail_model import SaleDetail
from app.models.sale_model import Sale
from app.models.update_product_log_model import UpdateProductLog
from app.models.user_model import User

from app import routes