#17. Implementar estructuras de datos b´asicas: pila, cola y lista enlazada.


def insertarPila(pila, elemento):
    pila.append(elemento)
    return pila

def eliminarPila(pila):
    elementoFinal = pila[len(pila)-1]
    pila.remove(elementoFinal)
    return pila


if __name__ == "__main__":
    estupila = list()
    insertarPila(estupila,1)
    print(estupila)
    insertarPila(estupila,"Que el poder de Python me acompañe en el semestre")
    print(estupila)
    insertarPila(estupila,"¡Profe, tenga piedad!")
    print(estupila)
    eliminarPila(estupila)
    print(estupila)

# Para cola
def insertarCola(cola, elemento):
    cola.append(elemento)
    return cola

def eliminarCola(cola):
    firstItem = cola[0]
    cola.remove(firstItem)
    return cola

contenedor = list()

insertarCola(contenedor, 12)
print(contenedor)
insertarCola(contenedor, 'Hay que pasar programación')
print(contenedor)
insertarCola(contenedor, 'Me gusta programación')
print(contenedor)
eliminarCola(contenedor)
print(contenedor)