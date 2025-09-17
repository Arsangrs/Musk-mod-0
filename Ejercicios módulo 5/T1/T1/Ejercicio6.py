materia=open("materia.txt", "r")

# Función para mostrar el contenido del archivo de texto materia.txt, y separar cada letra con un símbolo #
def hash_display():
    for linea in materia:        
        for letra in linea:      
            if letra != '\n':
                print(letra, end="#")
            else:
                print()
           
hash_display()
materia.close()