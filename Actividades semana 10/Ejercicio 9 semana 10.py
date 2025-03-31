# Ejercicio 9: Implementación de Múltiples Paradigmas
import operaciones
from persona import Persona

print("== Paradigma Imperativo ==")
numero1 = 10
numero2 = 5

if numero1 > numero2:
    print(f"{numero1} es mayor que {numero2}")
else:
    print(f"{numero2} es mayor que {numero1}")

suma = 0
for i in range(1, 6):
    suma += i
print(f"La suma de los primeros 5 números es: {suma}")

print("\n== Paradigma Estructurado ==")

def realizar_operaciones():
    a = 8
    b = 4

    print(f"La suma de {a} y {b} es: {operaciones.sumar(a, b)}")
    print(f"La resta de {a} y {b} es: {operaciones.restar(a, b)}")
    print(f"La multiplicación de {a} y {b} es: {operaciones.multiplicar(a, b)}")
    print(f"La división de {a} entre {b} es: {operaciones.dividir(a, b)}")

realizar_operaciones()
print("\n== Paradigma Orientado a Objetos ==")

persona = Persona("Renata", 18)
print(persona.saludar())

print(persona.cumpleaños())

