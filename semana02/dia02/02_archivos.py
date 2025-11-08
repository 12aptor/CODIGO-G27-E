archivo = open("alumnos.txt", "r")
contenido = archivo.read()
print(contenido)
print(type(contenido))
archivo.close()

archivo = open("alumnos.txt", "a")
archivo.write("\n")
archivo.write("2,Pedro,pedro@gmail.com,23")
archivo.close()

archivo = open("alumnos.txt", "w")
archivo.write("1,Ana,ana@gmail.com,25")
archivo.close()