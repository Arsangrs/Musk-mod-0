import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer datos 
meses = df["month_number"]
jabón = df["bathingsoap"]

# Crear gráfico de barras
plt.bar(meses, jabón, color="blue")

# Etiquetas de la gráfica
plt.xlabel("Número del mes")
plt.ylabel("Unidades de ventas en número")
plt.title("Ventas jabón de baño")
plt.xticks(range(1, 13))

# Cuadrícula
plt.grid(linestyle="-")

# Guardar gráfico en el disco
plt.savefig("bathingsoap_sales.png")

# Mostrar gráfica
plt.show()