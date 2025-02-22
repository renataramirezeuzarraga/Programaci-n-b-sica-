#24. Calcular la suma de una serie numérica.

print("Ingresa los siguientes datos, para crear la serie numérica: ")
a = float(input("Ingresa el primer término de la serie (a): "))
d = float(input("Ingresa el la diferencia de la serie (d): "))
n = int(input("Ingresa el número de término de la serie (n): "))

serie = []  
for i in range(n):
    termino = a + i * d  # Generar cada término
    serie.append(termino)

res = (n / 2) * (2 * a + (n - 1) * d)
print ("\nLa serie númerica es la siguiente:")
print (serie)
print (f" La suma de los primeros {n} términos de la serie númerica son {res}")