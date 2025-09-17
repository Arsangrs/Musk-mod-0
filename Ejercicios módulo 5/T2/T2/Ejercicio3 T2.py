import pandas as pd
import numpy as np

# Cargar el archivo
datos = pd.read_csv("Modulo5_Automobile_data_limpio.csv")

# Encontrar la fila con el precio máximo
fila_mayor_precio = datos.loc[datos['price'].idxmax()]

# Imprimir empresa y precio del coche más caro
print(f"Empresa: {fila_mayor_precio['company']}")
print(f"Precio: {fila_mayor_precio['price']}")