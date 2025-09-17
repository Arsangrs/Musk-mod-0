import numpy as np

sampleArray = np.array([[3, 6, 9, 12],[15, 18, 21, 24],[27, 30, 33, 36],[39, 42, 45, 48],[51, 54, 57, 60]])

# Filas impares 
filas_impares = sampleArray[1::2, :]

# Columnas pares 
resultado = filas_impares[:, 0::2]

print(resultado)