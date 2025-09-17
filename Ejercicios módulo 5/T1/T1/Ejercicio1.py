

poema = open("poema.txt","r",encoding="utf-8")

# Función para leer un archivo de texto y mostrar su contenido línea a línea en la consola
def funcionPoema():
    for linea in poema.readlines():
        print(linea)
funcionPoema()
poema.close()       