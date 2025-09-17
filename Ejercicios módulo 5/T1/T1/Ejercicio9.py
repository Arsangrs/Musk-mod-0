import string

def contar_frecuencia_palabras(nombre_archivo):
    frecuencias = {}

    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            # Eliminar puntuación y convertir a minúsculas
            linea = linea.translate(str.maketrans('', '', string.punctuation)).lower()
            palabras = linea.split()

            for palabra in palabras:
                if palabra in frecuencias:
                    frecuencias[palabra] += 1
                else:
                    frecuencias[palabra] = 1

    return frecuencias

# LLamada a la función, según el archivo de texto deseado
archivo = "poema.txt"  
frecuencias = contar_frecuencia_palabras(archivo)

# Mostrar resultados ordenados alfabéticamente
for palabra in sorted(frecuencias):
    print(f"{palabra}: {frecuencias[palabra]}")