import pandas as pd
import numpy as np

# Cargar el archivo
df = pd.read_csv("Modulo5_Automobile_data.csv")

# Crear lista de valores a reemplazar
valores_a_reemplazar = ["?", "n.a", "NaN"]

# Reemplazar por NaN de numpy
df.replace(valores_a_reemplazar, np.nan, inplace=True)

# Guardar el nuevo archivo con otro nombre
df.to_csv("Modulo5_Automobile_data_limpio.csv", index=False)

print("Archivo limpiado y guardado como 'Modulo5_Automobile_data_limpio.csv'")