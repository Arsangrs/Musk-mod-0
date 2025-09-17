import numpy as np

# Crear un array de números entre 100 y 200 con paso 10
valores = np.arange(100, 100 + 5*2*10, 10)

# Redimensionar a matriz 5x2
matriz = valores.reshape(5, 2)

print(matriz)