import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Lista de productos
productos = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]

# Nombres según gráfica de muestra
nombres = ["Crema Facial", "Lavado de cara", "Pasta de dientes", "Gel de baño", "Shampoo", "Moisturizer"]

# Calcular datos de ventas totales
ventas_totales = [df[producto].sum() for producto in productos]

# Crear gráfico circular
plt.pie(
    ventas_totales,
    labels=nombres,
    autopct="%1.1f%%",    # mostrar porcentaje     
)

# Título
plt.title("Sales data")

# Leyenda
plt.legend(loc="lower right")

# Mostrar gráfico
plt.show()