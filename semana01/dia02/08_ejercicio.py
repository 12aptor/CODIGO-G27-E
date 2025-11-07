""" Crear una aplicación para gestionar usuarios.
Donde podemos agregar, mostrar, actualizar y eliminar
usuarios (CRUD). """

import os

usuarios = {
    '78787878': {
        'nombre': 'Ana',
        'correo': 'ana@gmail.com'
    }
}

while True:
    os.system("clear")
    print("""
    ==============================
        GESTION DE USUARIOS
    ==============================
        [1] Agregar usuario
        [2] Mostrar usuarios
        [3] Actualizar usuario
        [4] Eliminar usuario
        [5] Salir
    """)
    opcion = int(input("Elija una opción: "))
    os.system("clear")
    
    if opcion == 1:
        dni = input("DNI: ")
        if dni in usuarios:
            print("El usuario ya existe")
        else:
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            usuarios[dni] = {
                'nombre': nombre,
                'correo': correo
            }
            print("usuario agregado correctamente")
        input("Presione enter para volver al menú")
    elif opcion == 2:
        for dni, usuario in usuarios.items():
            print(f"DNI: {dni}")
            print(f"Nombre: {usuario['nombre']}")
            print(f"Correo: {usuario['correo']}\n")
        
        input("Presione enter para volver al menú")
    elif opcion == 3:
        dni = input("DNI: ")
        if dni in usuarios:
            nombre = input("Nombre: ")
            correo = input("Correo: ")

            usuarios[dni] = {
                'nombre': nombre,
                'correo': correo
            }
            print("Usuario actualizado correctamente")
        else:
            print("Usuario no encontrado")
        input("Presione enter para volver al menú")
    elif opcion == 4:
        dni = input("DNI: ")
        if dni in usuarios:
            usuarios.pop(dni)
            print("Usuario eliminado correctamente")
        else:
            print("Usuario no encontrado")
        input("Presione enter para volver al menú")
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción incorrecta")
        input("Presione enter para volver al menú")