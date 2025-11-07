"""Crea una calculadora de operaciones aritméticas
(+, -, *, /). El programa debe pedir al usuario que ingrese
dos números y luego mostrar el resultado de la operación."""

numero1 = float(input("Primer número: "))
numero2 = float(input("Segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = numero1 + numero2
    print(resultado)
elif operacion == "-":
    resultado = numero1 - numero2
    print(resultado)
elif operacion == "*":
    resultado = numero1 * numero2
    print(resultado)
elif operacion == "/":
    if numero2 == 0:
        print("Error: No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2
        print(resultado)
else:
    print("Operación no válida")