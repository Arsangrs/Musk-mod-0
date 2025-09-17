import numpy as np

arrayOne = np.array([[5, 6, 9], [21, 18, 27]])
arrayTwo = np.array([[15, 33, 24], [4, 7, 111]])

# Sumar las dos matrices
resultado = arrayOne + arrayTwo

# Calcular el cuadrado de cada elemento
resultado_cuadrado = resultado ** 2

print("Suma de matrices:")
print(resultado)

print("\nCuadrado de la matriz resultado:")
print(resultado_cuadrado)