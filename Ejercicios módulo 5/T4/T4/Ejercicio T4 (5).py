import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer columnas 
meses = df["month_number"]
crema = df["facecream"]
lavado = df["facewash"]

# Acotar tamaño de la gráfica a la imagen dada
plt.figure(figsize=(6, 4))  

# Posición de las barras por mes
x = np.arange(len(meses))  # posiciones para cada mes
ancho = 0.30  # ancho de cada barra

# Crear gráfica de barras
plt.bar(x - ancho/2, crema, width=ancho, label="Ventas crema facial", color="blue")
plt.bar(x + ancho/2, lavado, width=ancho, label="Ventas lavado de cara", color="orange")

# Etiquetas de la gráfica
plt.xlabel("Número del mes")
plt.ylabel("Unidades de ventas en número")
plt.title("Facewash and facecream sales data")

# Números del mes
plt.xticks(x, meses)

# Cuadrícula
plt.grid(linestyle="-")

# Leyemda
plt.legend(loc="upper left")

# Mostrar gráfica
plt.show()