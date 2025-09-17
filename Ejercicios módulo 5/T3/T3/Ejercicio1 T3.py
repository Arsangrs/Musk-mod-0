import numpy as np 

# Crear array 4x2 de tipo unsignedint16
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8]], dtype=np.uint16)

# Imprimir atributos
print("Shape del array:", arr.shape)
print("Número de dimensiones:", arr.ndim)
print("Tamaño de cada elemento (bytes):", arr.itemsize)