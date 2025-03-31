#Ejercicio 8: Implementación de Mergesort
def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        medio = len(lista) // 2
        izquierda = lista[:medio]
        derecha = lista[medio:]

        izquierda = mergesort(izquierda)
        derecha = mergesort(derecha)

        return fusionar(izquierda, derecha)

def fusionar(izquierda, derecha):
    lista_ordenada = []
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] < derecha[j]:
            lista_ordenada.append(izquierda[i])
            i += 1
        else:
            lista_ordenada.append(derecha[j])
            j += 1

    while i < len(izquierda):
        lista_ordenada.append(izquierda[i])
        i += 1

    while j < len(derecha):
        lista_ordenada.append(derecha[j])
        j += 1

    return lista_ordenada

def main():
    numeros = input("Ingresa una lista de números separados por espacio: ")
    
    lista = [int(x) for x in numeros.split()]
    
    print("\nLista original:")
    print(lista)
    
    lista_ordenada = mergesort(lista)
    
    print("\nLista ordenada:")
    print(lista_ordenada)

if __name__ == "__main__":
    main()
