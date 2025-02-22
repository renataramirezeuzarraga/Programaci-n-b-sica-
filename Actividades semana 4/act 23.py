#23. Implementar y operar con matrices.

# Ponemos unas matrices predeterminadas 
matriz_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Para la suma de matrices
def sumar_matrices(matriz1, matriz2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        resultado = []
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz1[0])):
                fila.append(matriz1[i][j] + matriz2[i][j])
            resultado.append(fila)
        return resultado
    else:
        return "Las matrices deben tener las mismas dimensiones"

# Para la resta de matrices
def restar_matrices(matriz1, matriz2):
    if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
        resultado = []
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz1[0])):
                fila.append(matriz1[i][j] - matriz2[i][j])
            resultado.append(fila)
        return resultado
    else:
        return "Las matrices deben tener las mismas dimensiones"

# Para la multiplicacio de matrices
def multiplicar_matrices(matriz1, matriz2):
    if len(matriz1[0]) == len(matriz2):
        resultado = []
        for i in range(len(matriz1)):
            fila = []
            for j in range(len(matriz2[0])):
                suma = 0
                for k in range(len(matriz2)):
                    suma += matriz1[i][k] * matriz2[k][j]
                fila.append(suma)
            resultado.append(fila)
        return resultado
    else:
        return "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz"

# Traspuesta de una matriz
def transponer_matriz(matriz):
    resultado = []
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        resultado.append(fila)
    return resultado

# Imprimir matrices de manera legible
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)


print("Matriz A:")
imprimir_matriz(matriz_a)
print("\nMatriz B:")
imprimir_matriz(matriz_b)

print("\nSuma de A y B:")
imprimir_matriz(sumar_matrices(matriz_a, matriz_b))

print("\nResta de A y B:")
imprimir_matriz(restar_matrices(matriz_a, matriz_b))

print("\nMultiplicación de A y B:")
imprimir_matriz(multiplicar_matrices(matriz_a, matriz_b))

print("\nTranspuesta de la matriz A:")
imprimir_matriz(transponer_matriz(matriz_a))
