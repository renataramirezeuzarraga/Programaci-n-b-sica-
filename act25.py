#25. Generar y analizar histogramas de datos.

datos_input = input("Ingresa los datos separados por comas (por ejemplo: 12, 14, 15, 16, 18): ")
datos = [int(dato.strip()) for dato in datos_input.split(",")]

intervalos_input = input("Ingresa los intervalos separados por comas (por ejemplo: 10, 15, 20, 25): ")
intervalos = [int(intervalo.strip()) for intervalo in intervalos_input.split(",")]

# Crear el histograma (una lista con la frecuencia de cada intervalo)
histograma = [0] * (len(intervalos) - 1)

# Contar las frecuencias de cada intervalo
for dato in datos:
    for i in range(len(intervalos) - 1):
        if intervalos[i] <= dato < intervalos[i + 1]:
            histograma[i] += 1
            break

# Mostrar el histograma
print("\nHistograma:")
for i in range(len(intervalos) - 1):
    print(f"Intervalo {intervalos[i]} - {intervalos[i+1]}: {'*' * histograma[i]} ({histograma[i]})")

prom = sum(datos) / len(datos)
print(f"\El promedio de los datos: {prom}")

# Calcular la desviación estándar
sumcu = sum([(x - prom) ** 2 for x in datos])
desta = (sumcu / len(datos)) ** 0.5
print(f"Desviación estándar de los datos: {desta}")

