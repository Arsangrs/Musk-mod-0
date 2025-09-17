

# Función para añadir texto a un archivo y mostrar su contenido
def añadirTexto():
    with open("python.txt", "w+", encoding="utf-8") as python:
        python.write("Hola muindo")
        python.seek(0)  # Mover el cursor al inicio del archivo
        for linea in python.readlines():
            print(linea)

añadirTexto()
