""" Crear una aplicación que permita registrar, listar
actualizar y eliminar empresas """

import os

class Empresa:
    def create(self):
        name, email = self.get_data()
        with open("empresas.txt", "r") as archivo:
            lines = archivo.readlines()
            last_line = lines[-1]
            id = int(last_line.strip().split(",")[0])

        with open("empresas.txt", "a") as archivo:
            archivo.write(f"\n{id + 1},{name},{email}")

    def list(self):
        with open("empresas.txt", "r") as archivo:
            lines = archivo.readlines()
            for line in lines[1:]:
                datos = line.strip().split(",")
                id, name, email = datos
                print(f"ID: {id}")
                print(f"Nombre: {name}")
                print(f"Email: {email}\n")

    def update(self):
        id = self.get_id()

        updated_lines = ["id,nombre,email\n"]
        found = False

        with open("empresas.txt", "r") as archivo:
            lines = archivo.readlines()
            for line in lines[1:]:
                datos = line.strip().split(",")
                if id == int(datos[0]):
                    found = True
                    name, email = self.get_data()
                    updated_line = f"{id},{name},{email}\n"
                    updated_lines.append(updated_line)
                else:
                    updated_lines.append(line)

        if not found:
            print("Empresa no encontrada")
            return
        
        with open("empresas.txt", "w") as archivo:
            archivo.writelines(updated_lines)

    def delete(self):
        id = self.get_id()

        updated_lines = ["id,nombre,email\n"]
        found = False

        with open("empresas.txt", "r") as archivo:
            lines = archivo.readlines()
            for line in lines[1:]:
                datos = line.strip().split(",")
                if id == int(datos[0]):
                    found = True
                else:
                    updated_lines.append(line)
            
        if not found:
            print("Empresa no encontrada")
            return
        
        with open("empresas.txt", "w") as archivo:
            archivo.writelines(updated_lines)


    def get_data(self):
        name = input("Nombre: ")
        email = input("Email: ")
        return name, email
    
    def get_id(self):
        id = int(input("ID de la empresa: "))
        return id

def main():
    empresa = Empresa()

    while True:
        os.system("clear")
        print("""
====================================
    ADMINISTRADOR DE EMPRESAS
====================================
    [1] Registrar una empresa
    [2] Listar empresas
    [3] Actualizar una empresa
    [4] Eliminar una empresa
        """)
        opcion = int(input("Elegir una opcion: "))

        os.system("clear")

        match opcion:
            case 1:
                empresa.create()
            case 2:
                empresa.list()
            case 3:
                empresa.update()
            case 4:
                empresa.delete()
            case _:
                print("Opción invalida")

if __name__ == "__main__":
    main()
