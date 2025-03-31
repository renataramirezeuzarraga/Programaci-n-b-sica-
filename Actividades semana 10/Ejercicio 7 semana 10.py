#Ejercicio 7: Ordenamiento y Búsqueda
import random

def generar_lista(n, rango_min, rango_max):
    return [random.randint(rango_min, rango_max) for _ in range(n)]

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        menores = [x for x in lista[1:] if x <= pivot]
        mayores = [x for x in lista[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(mayores)

def busqueda_binaria(lista, objetivo):
    bajo = 0
    alto = len(lista) - 1
    while bajo <= alto:
        medio = (bajo + alto) // 2
        if lista[medio] == objetivo:
            return medio  
        elif lista[medio] < objetivo:
            bajo = medio + 1
        else:
            alto = medio - 1
    return -1  

def main():
    n = int(input("Ingresa el número de elementos para la lista: "))

    rango_min = int(input("Ingresa el valor mínimo para los números: "))
    rango_max = int(input("Ingresa el valor máximo para los números: "))
    
    lista = generar_lista(n, rango_min, rango_max)
    
    print("\nLista original:")
    print(lista)

    lista_ordenada = quicksort(lista)
    
    print("\nLista ordenada:")
    print(lista_ordenada)
    
    numero_buscar = int(input("\nIngresa el número que deseas buscar en la lista ordenada: "))
    
    indice = busqueda_binaria(lista_ordenada, numero_buscar)
    
    if indice != -1:
        print(f"El número {numero_buscar} se encuentra en la posición {indice} de la lista ordenada.")
    else:
        print(f"El número {numero_buscar} no se encuentra en la lista.")

if __name__ == "__main__":
    main()
