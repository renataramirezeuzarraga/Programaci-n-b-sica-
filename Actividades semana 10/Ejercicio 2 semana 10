#Ejercicio 2: Manejo de Inventario con Listas y Diccionarios
productos = []

def agregar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría del producto: ")
    precio = float(input("Precio del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    
    producto = {
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad
    }
    
    productos.append(producto)
    print("Producto agregado")

def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            print(f"Producto '{nombre}' eliminado.")
            return
    print("Producto no encontrado")

def buscar_producto():
    nombre = input("Nombre del producto a buscar: ")
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"Nombre: {producto['nombre']}")
            print(f"Categoría: {producto['categoria']}")
            print(f"Precio: {producto['precio']}")
            print(f"Cantidad: {producto['cantidad']}")
            return
    print("Producto no encontrado")

def mostrar_productos_ordenados():
    productos_ordenados = sorted(productos, key=lambda x: x["precio"])
    for producto in productos_ordenados:
        print(f"{producto['nombre']} - {producto['precio']}")

def mostrar_menu():
    while True:
        print("\nMenu:")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Buscar producto")
        print("4. Mostrar productos ordenados por precio")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            eliminar_producto()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            mostrar_productos_ordenados()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
            
mostrar_menu()
