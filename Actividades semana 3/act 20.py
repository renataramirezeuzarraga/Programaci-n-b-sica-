#20. Implementar b´usqueda binaria y lineal.

# Búsqueda Lineal Simple
def busqueda_lineal(arr, objetivo):
    for i in range(len(arr)):
        if arr[i] == objetivo:
            return i  # Devuelve el índice si lo encuentra
    return -1  # Si no lo encuentra, devuelve -1

# Búsqueda Binaria Simple
def busqueda_binaria(arr, objetivo):
    izquierda = 0
    derecha = len(arr) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # Encuentra el punto medio
        if arr[medio] == objetivo:
            return medio  # Si encuentra el objetivo, devuelve el índice
        elif arr[medio] < objetivo:
            izquierda = medio + 1  # Si el objetivo es mayor, busca en la mitad derecha
        else:
            derecha = medio - 1  # Si el objetivo es menor, busca en la mitad izquierda
    
    return -1  # Si no lo encuentra, devuelve -1

# Obtener lista y número a buscar del usuario
listanum = input("Introduce una lista de números separados por espacios: ")

# Convertir la entrada de texto en una lista de números
arr = listanum.split()  # Divide la entrada por espacios
arr = [int(num) for num in arr]  # Convierte cada elemento a un número entero

objetivo = int(input("Introduce el número que deseas buscar: "))

# Búsqueda Lineal
resulineal = busqueda_lineal(arr, objetivo)
if resulineal != -1:
    print(f"Elemento encontrado con búsqueda lineal en el índice {resulineal}")
else:
    print("Elemento no encontrado con búsqueda lineal")

# Búsqueda Binaria
arr.sort()  # Ordenamos la lista para la búsqueda binaria
resubinario = busqueda_binaria(arr, objetivo)
if resubinario != -1:
    print(f"Elemento encontrado con búsqueda binaria en el índice {resubinario}")
else:
    print("Elemento no encontrado con búsqueda binaria")
