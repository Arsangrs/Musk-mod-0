import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer datos
beneficio = df["total_profit"]

# Crear histograma
plt.figure(figsize=(6, 4))
plt.hist(beneficio, color="blue", label="Profit")

# Etiquetas de la gráfica
plt.xlabel("profit en dólares")
plt.ylabel("Actual Profit en dólares")
plt.title("Profit")
plt.ylim(0, 5)
plt.xlim(150000, 350000)

# Leyenda
plt.legend(loc="upper left")

# Mostrar gráfica
plt.show()