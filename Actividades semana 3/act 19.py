#19. Generar números aleatorios con distintas distribuciones.
from random import randint

aleP = list()
aleN = list()
ele = int(input("Introduce la cantidad de elementos: "))

for cont in range(-ele, ele):
    if cont < 0:
        aleN.append(randint(-100,0))
    elif cont > 0:
        aleP.append(randint(1,100))
    else:
        aleP.append(randint(0,1))
        
listaCompleta = aleN + aleP

print(listaCompleta)

