import numpy as np

sampleArray = np.array([[34, 43, 73],[82, 22, 12],[53, 94, 66]])

# Transponer para que sea columna 3x1
newColumn = np.array([[10, 10, 10]]).T  

# Eliminar la segunda columna
array_sin_columna = np.delete(sampleArray, 1, axis=1)

# Insertar newColumn en la posición 1
array_modificado = np.insert(array_sin_columna, 1, newColumn.flatten(), axis=1)

print(array_modificado)