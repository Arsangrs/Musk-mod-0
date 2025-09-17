import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer datos
meses = df["month_number"]

# Lista de productos
productos = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]

# Nombres para la leyenda
nombres = ["Crema Facial", "Lavado de cara", "Pasta de dientes", "Gel de baño", "Shampoo", "Moisturizer"]

# Colores según muiestra dada
colores = ["#972488", "#6AB5D3", "#FF0000", "#000000", "#008035", "#B9C572"]

# Crear el diagrama de pila 
plt.stackplot(meses, [df[producto] for producto in productos], labels=nombres, colors=colores)

# Etiquetas y título
plt.xlabel("Número de mes")
plt.ylabel("Unidades de ventas en número")
plt.title("Todas las ventas de productos en un stack plot")

# Leyenda
plt.legend(loc="upper left")

# Mostrar gráfico
plt.show()