#Ejercicio 5: Módulo para Conversión de Unidades
import conversor # type: ignore

def main():
    print("Bienvenido al conversor de unidades.")
    
    while True:
        print("\nElige una opción:")
        print("1. Convertir Kilómetros a Millas")
        print("2. Convertir Celsius a Fahrenheit")
        print("3. Convertir Litros a Galones")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            kilometros = float(input("Ingresa la cantidad de kilómetros: "))
            millas = conversor.km_a_millas(kilometros)
            print(f"{kilometros} kilómetros equivalen a {millas} millas.")
        
        elif opcion == "2":
            celsius = float(input("Ingresa la temperatura en Celsius: "))
            fahrenheit = conversor.celsius_a_fahrenheit(celsius)
            print(f"{celsius}° Celsius equivalen a {fahrenheit}° Fahrenheit.")
        
        elif opcion == "3":
            litros = float(input("Ingresa la cantidad de litros: "))
            galones = conversor.litros_a_galones(litros)
            print(f"{litros} litros equivalen a {galones} galones.")
        
        elif opcion == "4":
            print("Gracias por usar el conversor de unidades. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida, por favor ingresa una opción válida.")


if __name__ == "__main__":
    main()
