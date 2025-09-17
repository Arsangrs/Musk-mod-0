import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer datos
meses = df["month_number"]
gel_baño = df["bathingsoap"]
lavado_cara = df["facewash"]

# Crear entorno de las 2 gráficas
fig, axes = plt.subplots(2, 1, figsize=(6, 4))

# Gráfica de ventas gel de baño
axes[0].plot(meses, gel_baño, color="black", marker="o", linewidth=2, label="Bathing Soap")
axes[0].set_title("Ventas gel de baño")
axes[0].set_xticks(range(1, 13))
axes[0].set_yticks(range(7500, 12501, 2500))

# Gráfica de ventas lavado de cara
axes[1].plot(meses, lavado_cara, color="red", marker="o", linewidth=2, label="Face Wash")
axes[1].set_title("Ventas lavado de cara")
axes[1].set_ylabel("Unidades de ventas en número")
axes[1].set_xlabel("Número del mes")
axes[1].set_xticks(range(1, 13))
axes[1].set_yticks([1500, 2000])

# Ajustar salida
plt.tight_layout()

# Mostrar gráfica
plt.show()