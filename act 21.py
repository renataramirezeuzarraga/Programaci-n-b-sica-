#21. Calcular el ´area y volumen de distintas figuras geom´etricas.

def calcular_area_volumen():
    while True:
        print("\n¿Qué deseas hacer? Elige una de las siguientes opciones:")
        print("1. Calcular área")
        print("2. Calcular volumen")
        print("3. Salir")

        op = input("Opción: ")
        
        if op == "1":
            print("\nSelecciona la figura de la que quieres calcular el área:")
            print("1. Cuadrado")
            print("2. Rectángulo")
            print("3. Triángulo")
            print("4. Círculo")
            print("5. Rombo")
            print("6. Volver")
            
            a = input("Opción: ")
            
            if a == "1":
                lado = float(input("Lado: "))
                print(f"El área del cuadrado es: {lado ** 2}")

            elif a == "2":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print(f"El área del rectángulo es: {base * altura}")

            elif a == "3":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                print(f"El área del triángulo es: {(base * altura) / 2}")

            elif a == "4":
                radio = float(input("Radio: "))
                print(f"El área del círculo es: {3.14 * (radio ** 2)}")

            elif a == "5":
                dima = float(input("Diagonal mayor: "))
                dime = float(input("Diagonal menor: "))
                print(f"El área del rombo es: {(dima * dime) / 2}")

            elif a == "6":
                continue

            else:
                print("Opción no válida, intenta nuevamente.")
        
        elif op == "2":
            print("\nSelecciona la figura de la que quieres calcular el volumen:")
            print("1. Cubo")
            print("2. Prisma rectangular")
            print("3. Cilindro")
            print("4. Esfera")
            print("5. Cono")
            print("6. Volver")
            
            b = input("Opción: ")
            
            if b == "1":
                lado = float(input("Lado: "))
                print(f"El volumen del cubo es: {lado ** 3}")

            elif b == "2":
                base = float(input("Base: "))
                altura = float(input("Altura: "))
                profundidad = float(input("Profundidad: "))
                print(f"El volumen del prisma rectangular es: {base * altura * profundidad}")

            elif b == "3":
                radio = float(input("Radio: "))
                altura = float(input("Altura: "))
                print(f"El volumen del cilindro es: {3.14 * (radio ** 2) * altura}")

            elif b == "4":
                radio = float(input("Radio: "))
                print(f"El volumen de la esfera es: {(4/3) * 3.14 * (radio ** 3)}")

            elif b == "5":
                radio = float(input("Radio: "))
                altura = float(input("Altura: "))
                print(f"El volumen del cono es: {(1/3) * 3.14 * (radio ** 2) * altura}")

            elif b == "6":
                continue
            else:
                print("Opción no válida, intenta nuevamente.")
        
        elif op == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intenta nuevamente.")

calcular_area_volumen()
