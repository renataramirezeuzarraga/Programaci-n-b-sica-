#Ejercicio 6: Sistema de Gestión de Vehículos
class Vehiculo:
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrar_informacion(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: ${self.precio}")

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, precio, numero_puertas):
        super().__init__(marca, modelo, año, precio)
        self.numero_puertas = numero_puertas

    def mostrar_informacion(self):
        super().mostrar_informacion() 
        print(f"Número de puertas: {self.numero_puertas}")

class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, precio, cilindrada):
        super().__init__(marca, modelo, año, precio)
        self.cilindrada = cilindrada

    def mostrar_informacion(self):
        super().mostrar_informacion()  
        print(f"Cilindrada: {self.cilindrada} cc")

automovil = Automovil("Toyota", "Corolla", 2020, 20000, 4)

motocicleta = Motocicleta("Yamaha", "R1", 2021, 15000, 1000)

print("Información del Automóvil:")
automovil.mostrar_informacion()

print("\nInformación de la Motocicleta:")
motocicleta.mostrar_informacion()
