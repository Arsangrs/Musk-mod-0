import pandas as pd
import numpy as np

# Cargar el archivo
datos = pd.read_csv("Modulo5_Automobile_data_limpio.csv")

# Filtrar filas por la columna 'company' sea 'toyota' 
coches_toyota = datos[datos['company'].str.lower() == 'toyota']

# Mostrar los datos 
print(coches_toyota)