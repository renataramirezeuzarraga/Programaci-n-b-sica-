#14. Implementar distintos métodos de ordenamiento.
'''Tipos de ordenamiento 
1. Ordenamiento por Burbuja (Bubble Sort)
El algoritmo de ordenamiento por burbuja compara cada par de elementos adyacentes y los intercambia si están en el orden incorrecto. Este proceso se repite hasta que la lista está completamente ordenada.
2. Ordenamiento por Inserción (Insertion Sort)
En el ordenamiento por inserción, se toma un elemento de la lista y se coloca en su posición correcta, moviendo todos los elementos mayores hacia la derecha. Este proceso se repite para todos los elementos.
3. Ordenamiento por Selección (Selection Sort)
El algoritmo de ordenamiento por selección encuentra el elemento más pequeño (o más grande) y lo coloca en la primera posición. Luego, encuentra el siguiente elemento más pequeño y lo coloca en la segunda posición, y así sucesivamente.
4. Ordenamiento Rápido (QuickSort)
El algoritmo de ordenamiento rápido es un algoritmo de ordenamiento eficiente que utiliza la técnica de "divide y vencerás". Elige un "pivote" y divide la lista en dos sublistas: una con los elementos menores al pivote y otra con los elementos mayores al pivote. Luego, ordena recursivamente esas sublistas.
'''
# 1. Ordenamiento por Burbuja (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 2. Ordenamiento por Inserción (Insertion Sort)
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# 3. Ordenamiento por Selección (Selection Sort)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# 4. Ordenamiento Rápido (QuickSort)
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Lista desordenada para probar
arr = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", arr)

# Aplicar Bubble Sort
arr_bubble = arr.copy()
bubble_sort(arr_bubble)
print("Ordenado con Bubble Sort:", arr_bubble)

# Aplicar Insertion Sort
arr_insertion = arr.copy()
insertion_sort(arr_insertion)
print("Ordenado con Insertion Sort:", arr_insertion)

# Aplicar Selection Sort
arr_selection = arr.copy()
selection_sort(arr_selection)
print("Ordenado con Selection Sort:", arr_selection)

# Aplicar QuickSort
arr_quick = arr.copy()
sorted_arr_quick = quick_sort(arr_quick)
print("Ordenado con QuickSort:", sorted_arr_quick)
