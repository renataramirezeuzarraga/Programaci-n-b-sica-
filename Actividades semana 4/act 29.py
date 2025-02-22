#29. Generar y analizar datos estadísticos

# Solicitar los datos al usuario
datosin = input("Ingresa los datos separados por comas (por ejemplo: 1, 2, 3, 4, 5): ")
datos = [float(dato.strip()) for dato in datosin.split(",")]

# Calcular la media
media = sum(datos) / len(datos)

# Calcular la mediana
datosor = sorted(datos)
n = len(datos)
if n % 2 == 0:
    mediana = (datosor[n // 2 - 1] + datosor[n // 2]) / 2
else:
    mediana = datosor[n // 2]

# Calcular la moda
frecuencia = {}
for num in datos:
    if num in frecuencia:
        frecuencia[num] += 1
    else:
        frecuencia[num] = 1
max_frecuencia = max(frecuencia.values())
moda = [num for num, freq in frecuencia.items() if freq == max_frecuencia]

# Calcular la desviación estándar
suma_cuadrados = sum([(x - media) ** 2 for x in datos])
desviacion_estandar = (suma_cuadrados / len(datos)) ** 0.5

# Calcular la varianza
varianza = desviacion_estandar ** 2

# Mostrar los resultados
print("\nAnálisis de los datos:")
print(f"Datos ingresados: {datos}")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Moda: {moda}")
print(f"Desviación estándar: {desviacion_estandar}")
print(f"Varianza: {varianza}")
