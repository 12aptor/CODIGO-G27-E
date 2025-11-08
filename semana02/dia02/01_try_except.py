""" Maneje de excepciones """

# division = 10 / 0
# print(division)

# Bloque try: Sirve para ejecutar una seccion de codigo
try:
    division = 10 / 0
# Bloque except: Sirve para capturar una excepcion
except ZeroDivisionError as error:
    print(error)
except Exception as error:
    print(error)
# Bloque finally: Se ejecutará siempre al finalizar
finally:
    print("El bloque finally se ejecutó")

print("El bloque try-except se ejecutó")