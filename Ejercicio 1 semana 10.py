#Ejercicio 1: Análisis de Texto con Diccionarios y Conjuntos

def analisis_texto(texto):
    palabras = texto.lower().split()
    total_palabras=len(palabras)
    palabras_unicas=set(palabras)

    frecuencia_palabras={}
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1

    palabra_mas_frecuente = max(frecuencia_palabras, key=frecuencia_palabras.get)
    frecuencia_palabra_mas_frecuente = frecuencia_palabras[palabra_mas_frecuente]

    # Imprimir los resultados
    print(f"Total de palabras: {total_palabras}")
    print(f"Palabras únicas: {len(palabras_unicas)}")
    print("Frecuencia de palabras:")
    for palabra, frecuencia in frecuencia_palabras.items():
        print(f"{palabra}: {frecuencia}")
        
    print(f"La palabra más frecuente es '{palabra_mas_frecuente}' con {frecuencia_palabra_mas_frecuente} apariciones.")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Ingresa un texto: ")

analisis_texto(texto_usuario)
