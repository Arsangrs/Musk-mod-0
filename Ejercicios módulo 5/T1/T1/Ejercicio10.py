import os

# Nombre del archivo a comprobar
nombre_archivo = "poema.txt" 

# Comprobar si el archivo existe y mostrarlo en la consola
if os.path.exists(nombre_archivo):
    print(f"El archivo '{nombre_archivo}' exite.")
else:
    print(f"El archivo '{nombre_archivo}' no existe.")