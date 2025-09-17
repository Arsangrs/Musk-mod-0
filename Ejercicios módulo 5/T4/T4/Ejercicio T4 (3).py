import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Lista de productos 
productos = ["facecream", "facewash", "toothpaste", "bathingsoap", "shampoo", "moisturizer"]

# Generar línea por producto
for producto in productos:
    plt.plot(
        df["month_number"],       # Meses 
        df[producto],             # Ventas 
        marker="o",               # marcador círculo
        linewidth=3,              # ancho de línea
        label=producto.capitalize()  # etiqueta para la leyenda
    )

# Etiquetas de ejes y título
plt.xlabel("Número mes")
plt.ylabel("Unidades de ventas en número")
plt.title("Ventas")

# Leyenda
plt.legend(loc="upper left")

# Mostrar gráfica
plt.show()