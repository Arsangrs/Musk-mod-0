import numpy as np

# Crear array de 24 elementos desde 10 con paso 1
arr = np.arange(10, 10 + 24).reshape(8, 3)

print("Matriz original 8x3:")
print(arr)

# Dividir en 4 submatrices por filas 
submatrices = np.array_split(arr, 4, axis=0)

print("\nSubmatrices:")
for i, sm in enumerate(submatrices, 1):
    print(f"\nSubmatriz {i}:")
    print(sm)