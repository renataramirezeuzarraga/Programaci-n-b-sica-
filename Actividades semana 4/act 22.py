#22. Simular el lanzamiento de un dado y una moneda.

import random

def lanzar_dado():
    return random.randint(1, 6)  # El dado tiene 6 caras

def lanzar_moneda():
    return random.choice(["Cara", "Cruz"])  # Puede ser "Cara" o "Cruz"

while True:
    print("\nSimulador de Lanzamientos\n")
    print("1. Lanzar un dado")
    print("2. Lanzar una moneda")
    print("3. Salir")

    opcion = input("Opción: ")


    if opcion == '1':
        # Lanzar el dado
        print ("\nLanzar un dado")
        resdado = lanzar_dado()
        print(f"El resultado del dado es: {resdado}")

    elif opcion == '2':
        # Lanzar la moneda
        print("\nLanzar una moneda")
        resmone = lanzar_moneda()
        print(f"El resultado de la moneda es: {resmone}")

    elif opcion == '3':
        print("Saliendo del programa...")
        break   
    
    else:
        print("Opción no válida, por favor selecciona una opción válida.")
    
    print()  # Salto de línea para claridad
