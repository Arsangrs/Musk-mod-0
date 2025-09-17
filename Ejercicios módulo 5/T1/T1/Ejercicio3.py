
historia = open("historia.txt","r")

# Función para contar el número de palabras en un archivo de texto 
def funcionHistoria():  
    palabras=0
    for linea in historia:  
        for palabra in linea.lower().split():
            palabras+=1        
    print("En el texto hay",palabras,"palabras")
funcionHistoria()
historia.close()    