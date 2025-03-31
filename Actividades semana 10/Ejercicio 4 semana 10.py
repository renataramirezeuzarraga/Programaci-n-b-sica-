#Ejercicio 4: Calculadora de Estadísticas
import math

def calcular_estadisticas(*args):
    if len(args) == 0:
        print("No se han ingresado números.")
        return

    promedio = (lambda nums: sum(nums) / len(nums))(args)  

    nums_ordenados = sorted(args)  
    n = len(nums_ordenados)
    if n % 2 == 1:
        mediana = nums_ordenados[n // 2]
    else:
        mediana = (nums_ordenados[n // 2 - 1] + nums_ordenados[n // 2]) / 2

    desviacion_estandar = (lambda nums, prom: math.sqrt(sum((x - prom) ** 2 for x in nums) / len(nums)))(args, promedio)

    print(f"Promedio: {promedio}")
    print(f"Mediana: {mediana}")
    print(f"Desviación Estándar: {desviacion_estandar}")

entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
try:
    numeros = list(map(float, entrada_usuario.split()))
    
    calcular_estadisticas(*numeros)

except ValueError:
    print("Por favor, ingresa solo números válidos.")
