import pandas as pd

# Cargar el archivo
df = pd.read_csv("Modulo5_Automobile_data.csv")  

# Imprimir las primeras 5 líneas
print("Primeras 5 filas:")
print(df.head())

# Imprimir las primeras 5 líneas
print("\nÚltimas 5 filas:")
print(df.tail())