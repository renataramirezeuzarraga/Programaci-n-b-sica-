#15. Determinar si un a˜no es bisiesto.

anio=int(input("Ingresa el año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
 print (f"{anio} es un año bisiesto")
else:
 print (f"{anio} no es un año bisiesto")

