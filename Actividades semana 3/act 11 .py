#11. Verificar si una cadena es un palíndromo.

y=input('Escribe una palabra: ').lower()

if y==y[::-1]:
  print("La palabra " +y+ " es un Palíndromo")
else:
  print ("La palabra " +y+ " no es un Palíndromo")