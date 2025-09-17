import pandas as pd
import matplotlib.pyplot as plt 

# Leer el archivo Modulo5_company_sales_data.csv
data = pd.read_csv("Modulo5_company_sales_data.csv")

 #Extraer columnas solicitadas
months = data['month_number']          
profits = data['total_profit']          

# Dibujar gráfico de líneas
plt.figure(figsize=(10, 5))  
plt.plot(months, profits, color='blue', linestyle='-', linewidth=2)

# Crear etiquetas
plt.xlabel("Número de mes")
plt.ylabel("Beneficio total")
plt.title("Beneficio por mes")
plt.xticks(months) 
plt.yticks([100000, 200000, 300000, 400000, 500000])

# Mostrar gráfica
plt.show()