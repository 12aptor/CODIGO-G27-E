def sumar(a, b):
    return a + b

# resultado = sumar(5, 10)
# print(resultado)

""" Funciones con valores por defecto """
def saludar(nombre="invitado"):
    print(f"¡Hola {nombre}!")

saludar(nombre="Ana")

""" Funciones con n argumentos (*args) """
def mostrar_numeros(*numeros):
    for numero in numeros:
        print(numero)

# mostrar_numeros(1, "Hola", True)


""" Funciones con n argumentos con nombres (**kwargs) """
def mostrar_info(**info):
    print(info.items())
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=30, correo="ana@gmail.com")