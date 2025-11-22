from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func

app = Flask(__name__)
db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/flask-sqlalchemy'

db.init_app(app)

class UserModel(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    created_at = Column(DateTime, default=func.now())

with app.app_context():
    db.create_all()

@app.route('/users', methods=['GET', 'POST'])
def home():
    method = request.method
    if method == 'GET':
        users = UserModel.query.all()

        response = []
        for user in users:
            response.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'created_at': str(user.created_at)
            })
        return {
            'message': 'Users fetched successfully',
            'data': response
        }, 200

if __name__ == '__main__':
    app.run(debug=True)