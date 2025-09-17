
historia = open("historia.txt","r")

# Función para contar el número de líneas en un archivo de texto historia.txt
def funcionHistoria():  
    lineas=0
    for linea in historia:  
        lineas+=1        
    print("En el texto hay",lineas,"lineas")
funcionHistoria()
historia.close()    