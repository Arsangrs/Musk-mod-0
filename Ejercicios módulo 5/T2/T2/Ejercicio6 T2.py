import pandas as pd
import numpy as np

# Cargar el archivo
datos = pd.read_csv("Modulo5_Automobile_data_limpio.csv")

# Encontrar la fila con el precio máximo
fila_mayor_precio = datos.loc[datos.groupby('company')['price'].idxmax()]

# Imprimir los resultados indicados
for _, fila in fila_mayor_precio.iterrows():
    print(f"Empresa: {fila['company']}, Coche: {fila['body-style']}, Precio: {fila['price']}")