import pandas as pd
import numpy as np

# Cargar el archivo
datos = pd.read_csv("Modulo5_Automobile_data_limpio.csv")

# Ordenar por precio descendente
datos_ordenados = datos.sort_values(by='price', ascending=False)

# Mostrar los datos ordenados de mayor a menor precio
print(datos_ordenados)