#27. Crear un conversor de unidades

def conversor_unidades():
    while True:
        print("\nConversor de Unidades de Longitud")
        print("1. Convertir de metros a centímetros")
        print("2. Convertir de metros a kilómetros")
        print("3. Convertir de centímetros a metros")
        print("4. Convertir de centímetros a kilómetros")
        print("5. Convertir de kilómetros a metros")
        print("6. Convertir de kilómetros a centímetros")
        print("7. Salir")

        op = input("Opción: ")
        
        if op == "1":
            print("\nConvertir de metros a centímetros\n")
            m = float(input("Cantidad de metros: "))
            cm = m*100
            print(f"{m} m = {cm} cm") 
                  
        elif op == "2":
            print("\nConvertir de metros a kilómetros\n")
            m = float(input("Cantidad de metros: "))
            km = m/100
            print(f"{m} m = {km} km") 
        
        elif op == "3":
            print("\nConvertir de centímetros a metros\n")
            cm = float(input("Cantidad de centimetros: "))
            m = cm/100
            print(f"{cm} cm = {m} m") 
        
        elif op == "4":
            print("\nConvertir de centímetros a kilómetros\n")
            cm = float(input("Cantidad de centimetros: "))
            km = cm/100000
            print(f"{cm} cm = {km} km") 
        
        elif op == "5":
            print("\nConvertir de kilómetros a metros\n")
            km = float(input("Cantidad de kilometros: "))
            m = km*1000
            print(f"{km} km = {m} m") 

        elif op == "6":
            print("\nConvertir de kilómetros a centímetros\n")
            km = float(input("Cantidad de kilometros: "))
            cm = km*100000
            print(f"{km} km = {cm} cm") 
        
        elif op == "7":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, intentalo otra vez ")


conversor_unidades()