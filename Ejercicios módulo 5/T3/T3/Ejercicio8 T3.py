import numpy as np

sampleArray = np.array([[34, 43, 73],[82, 22, 12],[53, 94, 66]])

max_eje0 = np.max(sampleArray, axis=0)
min_eje1 = np.min(sampleArray, axis=1)

print("Máximo por columna (eje 0):", max_eje0)
print("Mínimo por fila (eje 1):", min_eje1)