#10. Leer, escribir y modificar un archivo de texto.

with open("archivo.txt", "w") as archivo:
    archivo.write("linea 1: Hola, este es un archivo de texto.\n")
    archivo.write("linea 2: quiero pasar programacion")

# Leer el archivo (modo 'r' solo lectura)
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("contenido del archivo:")
    print(contenido)

# Agregar más líneas al archivo (modo 'a' para añadir al final)
with open("archivo.txt", "a") as archivo:
    archivo.write("\nlinea 3: podemos escribir aqui.\n")
    archivo.write("linea 4: podemos seguir escribiendo aqui.\n")

# Imprimir lo nuevo que se escribió
print("lo nuevo que escribimos es:")

# Leer el archivo nuevamente para mostrar lo agregado
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
