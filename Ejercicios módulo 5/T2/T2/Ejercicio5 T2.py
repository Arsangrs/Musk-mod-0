import pandas as pd
import numpy as np

# Cargar el archivo
datos = pd.read_csv("Modulo5_Automobile_data_limpio.csv")

# Filtrar filas por la columna 'company' valores
coches_empresa = datos['company'].value_counts()

# Mostrar los datos 
print(coches_empresa)