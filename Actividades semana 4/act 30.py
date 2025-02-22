#30. Implementar funciones recursivas.

#Ejemplo de funciones recurivas (2 ejemplos)

#Ejemplo 1
def factorial(n):
   if n == 0: 
       return 1
   else:
       return n * factorial(n - 1) 

#Muestra el factorial
num=int(input("Ingresa el número para sacar el factorial: "))

print(f"El factorial de {num} es {factorial(num)}")

#Ejemplo 2
def potencia(a, b):
    if b == 0:
        return 1
    
    else:
        return a * potencia(a, b - 1)

base = int(input("Ingresa la base (a): "))
exp = int(input("Ingresa el exponente (b): "))

# Calcular la potencia y mostrar el resultado
resultado = potencia(base, exp)
print(f"{base} elevado a la potencia de {exp} es {resultado}")

