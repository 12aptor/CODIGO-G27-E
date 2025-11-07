""" Crear una aplicación que simule ser un cajero
automático, del cual puedas retirar y depositar dinero,
además debe ser posible ver el saldo. """

import os

class Cajero:
    def __init__(self):
        self.saldo = 1000
    
    def retirar(self, cantidad):
        if cantidad > self.saldo:
            print("Saldo insuficiente")
            return
        self.saldo -= cantidad
        print(f"Retirado {cantidad}")

    def depositar(self, cantidad):
        if cantidad <= 0:
            print("Cantidad incorrecta")
            return
        self.saldo += cantidad
        print(f"Depositado {cantidad}")

    def ver_saldo(self):
        print(f"Saldo: {self.saldo}")

cajero = Cajero()

while True:
    os.system("clear")
    
    print("""
    CAJERO AUTOMÁTICO
        1. Retirar dinero
        2. Depositar dinero
        3. Ver saldo
    """)
    opcion = int(input("Opción: "))
    if opcion == 1:
        cantidad = int(input("Cantidad a retirar: "))
        cajero.retirar(cantidad)
    elif opcion == 2:
        cantidad = int(input("Cantidad a depositar: "))
        cajero.depositar(cantidad)
    elif opcion == 3:
        cajero.ver_saldo()
    else:
        print("Opción incorrecta")
    
    input("Pulsa ENTER para continuar...")
