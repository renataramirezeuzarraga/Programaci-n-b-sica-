#26. Implementar una agenda de contactos.
bandera=True 
contador =1
listacontactos=list()

while bandera:
    op= input("Cantidad de contactos: {contador} \n Desea agregar un contacto?(Si/No): ")
    if op.lower() == "si":
        contacto =dict()
        contacto["identificador"]=input(f"Ingrese el identificador del contacto {contador}: ")
        contacto ["numero"]=input(f"Ingrese el número del contacto {contador}: ")
        contador+=1
        listacontactos.append(contacto)
    else:
        break

print(listacontactos)