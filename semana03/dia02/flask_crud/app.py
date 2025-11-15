from flask import Flask, request

app = Flask(__name__)

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
        }
    
    elif method == 'GET':
        # Obtener todos los usuarios
        return {
            'ok': True,
            'message': 'Lista de usuarios obtenida correctamente',
            'data': usersList
        }

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
                }
        return {
            'ok': False,
            'message': 'Usuario no encontrado',
            'data': None
        }
            
    elif method == 'PUT':
        # Actualizar un usuario
        pass
    elif method == 'DELETE':
        # Eliminar un usuario
        pass

if __name__ == '__main__':
    app.run(debug=True)