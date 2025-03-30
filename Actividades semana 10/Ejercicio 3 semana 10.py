#Ejercicio 3: Gestión de Contactos con Tuplas y Estructuras Anidadas

agenda_contactos = []

def agregar_contacto():
    nombre = input("Nombre del contacto: ")
    numero = input("Número del contacto: ")
    correo = input("Correo del contacto: ")
    
    contacto = (nombre, numero, correo)
    agenda_contactos.append(contacto)
    print("Contacto agregado")

def buscar_contacto():
    nombre = input("Nombre del contacto a buscar: ")
    encontrado = False
    for contacto in agenda_contactos:
        if contacto[0].lower() == nombre.lower():  
            print(f"Nombre: {contacto[0]}")
            print(f"Número: {contacto[1]}")
            print(f"Correo: {contacto[2]}")
            encontrado = True
            break
    if not encontrado:
        print("Contacto no encontrado")


def listar_contactos():
    agenda_contactos.sort(key=lambda contacto: contacto[0].lower())  
    for contacto in agenda_contactos:
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

def mostrar_menu():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Listar todos los contactos")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            listar_contactos()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

mostrar_menu()
