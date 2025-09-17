
story=open("story.txt", "r")

# Función para mostrar las palabras de un archivo de texto que tienen menos de 4 carácteres
def display_words():
    for linea in story:
        palabras = linea.split()
        for palabra in palabras:
            if len(palabra) < 4:
                print(palabra)
display_words()
story.close()

