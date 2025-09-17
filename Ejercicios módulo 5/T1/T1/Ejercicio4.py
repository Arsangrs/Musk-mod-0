
notas = open("notas.txt","r")

# Función para contar el número de veces que aparece la palabra "el" en el archivo de texto notas.txt
def funcionNotas():  
    palabras=0
    for linea in notas:  
        for palabra in linea.lower().split():
            
            if palabra == "el":
                palabras+=1
                
            else:
                pass           
            
    print("En el texto hay",palabras,"el")         
    
funcionNotas()
notas.close()    



