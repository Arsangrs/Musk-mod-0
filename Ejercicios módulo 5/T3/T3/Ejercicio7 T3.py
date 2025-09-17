import numpy as np

sampleArray = np.array([[34, 43, 73],[82, 22, 12],[53, 94, 66]])

# Primer caso
# Obtener índices que ordenan la segunda fila
indices = np.argsort(sampleArray[1, :])

# Ordenar columnas según esos índices
ordenado_por_fila = sampleArray[:, indices]

print("Array ordenado por la segunda fila:")
print(ordenado_por_fila)

# Segundo caso
# Obtener índices que ordenan la segunda columna
indices = np.argsort(sampleArray[:, 1])

# Ordenar filas según esos índices
ordenado_por_columna = sampleArray[indices, :]

print("\nArray ordenado por la segunda columna:")
print(ordenado_por_columna)