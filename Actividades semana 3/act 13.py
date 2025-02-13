#13. Convertir una temperatura entre distintas escalas

def convertir_temperatura():
    while True:
        print("\nConversión de Temperatura")
        print ("Elige una de las siguientes opciones: ")
        print("  1. Celsius a Fahrenheit")
        print("  2. Fahrenheit a Celsius")
        print("  3. Celsius a Kelvin")
        print("  4. Kelvin a Celsius")
        print("  5. Fahrenheit a kelvin")
        print("  6. Kelvin a Fahrenheit")
        print("  7. Salir")

        menu = input()

        if menu == "1":
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C es igual a {fahrenheit}°F")
        
        elif menu == "2":
            fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F es igual a {celsius}°C")
        
        elif menu == "3":
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            kelvin = celsius + 273.15
            print(f"{celsius}°C es igual a {kelvin} K")
        
        elif menu == "4":
            kelvin = float(input("Ingresa la temperatura en Kelvin: "))
            celsius = kelvin - 273.15
            print(f"{kelvin} K es igual a {celsius}°C")
        
        elif menu == "5":
            fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
            kelvin = ((fahrenheit-32)/1.8)+273.15
            print(f"{fahrenheit}°F es igual a {kelvin} K")
        
        elif menu == "6":
            kelvin = float(input("Ingresa la temperatura en Kelvin: "))
            fahrenheit = ((kelvin-273.15)*1.8)+32
            print(f"{kelvin} K es igual a {fahrenheit} °F")

        elif menu == "7":
            break 
        
        else:
            print("Opción no válida, por favor elige una opción del 1 al 7")

convertir_temperatura()
