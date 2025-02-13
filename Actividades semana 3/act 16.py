#16. Contar el número de vocales y consonantes en una cadena.

word=str(input("Ingresa una palabra: "))

vocales=("aeiouAEIOU")


numvocales=0
numconsonantes=0
for caracter in word:
    if caracter in vocales:
        numvocales += 1
    else:
        numconsonantes+=1

print(f"Número de vocales: {numvocales}")
print(f"Número de consonantes: {numconsonantes}")
