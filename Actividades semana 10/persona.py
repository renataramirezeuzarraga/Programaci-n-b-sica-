# persona.py

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años."

    def cumpleaños(self):
        self.edad += 1
        return f"Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."
