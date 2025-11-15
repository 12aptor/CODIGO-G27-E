from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

usersList = []

@app.route('/')
def home():
    return 'Hello World! 🐍'

@app.route('/users', methods=['GET', 'POST'])
def users():
    method = request.method
    if method == 'POST':
        # Crear un nuevo usuario
        json = request.get_json()
        json['id'] = len(usersList) + 1
        usersList.append(json)
        return {
            'ok': True,
            'message': 'Usuario creado correctamente',
            'data': json
        }, 200
    
    elif method == 'GET':
        # Obtener todos los usuarios
        return {
            'ok': True,
            'message': 'Lista de usuarios obtenida correctamente',
            'data': usersList
        }, 200

@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def user(id):
    method = request.method
    if method == 'GET':
        # Obtener un usuario
        for user in usersList:
            if user['id'] == id:
                return {
                    'ok': True,
                    'message': 'Usuario obtenido correctamente',
                    'data': user
                }, 200
        return {
            'ok': False,
            'message': 'Usuario no encontrado',
            'data': None
        }, 404
            
    elif method == 'PUT':
        # Actualizar un usuario
        json = request.get_json()
        for user in usersList:
            if user['id'] == id:
                user['name'] = json['name']
                user['email'] = json['email']
                user['password'] = json['password']
                return {
                    'ok': True,
                    'message': 'Usuario actualizado correctamente',
                    'data': user
                }, 200
        return {
            'ok': False,
            'message': 'Usuario no encontrado',
            'data': None
        }, 404
    
    elif method == 'DELETE':
        # Eliminar un usuario
        for user in usersList:
            if user['id'] == id:
                usersList.remove(user)
                return {
                    'ok': True,
                    'message': 'Usuario eliminado correctamente',
                    'data': None
                }, 200
        return {
            'ok': False,
            'message': 'Usuario no encontrado',
            'data': None
        }, 404

if __name__ == '__main__':
    app.run(debug=True)