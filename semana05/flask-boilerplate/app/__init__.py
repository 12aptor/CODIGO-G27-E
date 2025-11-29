from flask import Flask
from flask_migrate import Migrate
from db import db
from config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app.models.role_model import Role
from app.models.user_model import User

from app import routes