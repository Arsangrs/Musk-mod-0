import pandas as pd

# Diccionarios como dataframes
car_Price = pd.DataFrame ({'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],'Price': [23845, 17995, 135925, 71400]})

car_Horsepower = pd.DataFrame ({'Company': ['Toyota', 'Honda', 'BMW', 'Audi'],'horsepower': [141, 80, 182, 160]})

# Fusionar los DataFrames por la columna 'Company'
dataframe_combinado = pd.merge(car_Price, car_Horsepower, on='Company')

print(dataframe_combinado)