import pandas as pd
import matplotlib.pyplot as plt

# Leer archivo Modulo5_company_sales_data.csv
df = pd.read_csv("Modulo5_company_sales_data.csv")

# Extraer columnas del archivo
meses = df['month_number']
beneficio = df['total_profit']

# Calcular el beneficio total
beneficio_total = beneficio.sum()
print("Beneficio total de todos los meses:", beneficio_total)

# Opciones para generar la gráfica
plt.figure(figsize=(8, 4))  
plt.plot(
    meses,                      # Meses del año
    beneficio,                  # Beneficio por mes
    linestyle="--",             # Línea discontinua
    color="red",                # Color de la línea
    linewidth=3,                # Ancho de la línea     
    marker="o",                 # Marcador de puntos
    markerfacecolor="black",    # Color del marcador    
    label="Profit data of last year" # Etiqueta leyenda                   
)

# Etiquetas de la gráfica
plt.title("Beneficio por mes")
plt.xlabel("Número de mes")
plt.ylabel("Beneficio total")

# Leyenda 
plt.legend(loc="lower right")

# Mostrar gráfica
plt.show()