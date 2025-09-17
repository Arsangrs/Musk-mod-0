

import string, os

# Función para crear archivos de texto con letras del abecedario 
def funcionCrearArchivos(Ejercicio7):
    for letra in string.ascii_uppercase:
        with open(os.path.join("Ejercicio7", "%s.txt" % letra), "w", encoding="utf-8") as letras:
            letras.writelines(letra)                  
       
    
Ejercicio7="letras"
funcionCrearArchivos(Ejercicio7)
