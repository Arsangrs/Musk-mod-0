import pandas as pd
import numpy as np

# Cargar el archivo
datos = pd.read_csv("Modulo5_Automobile_data_limpio.csv")

# Filtrar y agrupar filas por la columna 'company' y kilometraje medio
kilometraje_medio = datos.groupby('company')['average-mileage'].mean()

# Mostrar los datos 
print(kilometraje_medio)