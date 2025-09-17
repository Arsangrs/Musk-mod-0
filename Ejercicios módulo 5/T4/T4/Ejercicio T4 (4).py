import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer columnas
meses = df["month_number"]
ventas_pasta_dientes = df["toothpaste"]

# Grafica de dispersión
plt.scatter(meses, ventas_pasta_dientes, color="blue", label="Ventas de pasta de dientes")

# Etiquetas de la gráfica
plt.xlabel("Número del mes")
plt.ylabel("Número de unidades vendidas")
plt.title("Ventas pasta de dientes")

# Leyenda
plt.legend(loc="upper left")

# Cuadrícula
plt.grid(linestyle="-")

# Mostrar gráfica
plt.show()