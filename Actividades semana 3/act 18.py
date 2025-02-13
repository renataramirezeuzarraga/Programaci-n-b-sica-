#18. Resolver ecuaciones cuadráticas.

import cmath

print("Dada la forma ax²+bx+c ingresa los valores: ")
a=int(input("Ingresa el valor de a: "))
b=int(input("Ingresa el valor de b: "))
c=int(input("Ingresa el valor de c: "))

x1= (-b+(cmath.sqrt(b**2-4*a*c)))/ (2*a)
x2= (-b-(cmath.sqrt(b**2-4*a*c)))/ (2*a)

print(f"Dada la ecuación {a}x²+{b}x+{c}las soluciones son las siguientes: ")
print(f"Solución 1 = {x1}")
print(f"Solución 2 = {x2}")