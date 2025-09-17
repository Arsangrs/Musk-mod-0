import pandas as pd

# DataFrame con coches GermanCars
GermanCars = pd.DataFrame({'Company': ['Ford', 'Mercedes', 'BMW', 'Audi'],'Price': [23845, 171995, 135925, 71400]})

# DataFrame con coches JapaneseCars 
JapaneseCars = pd.DataFrame({'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi'],'Price': [29995, 23600, 61500, 58900]})

# Concatenar los dos DataFrames
coches_dataframes = pd.concat([GermanCars, JapaneseCars])

# Mostrar el DataFrame concatenado
print(coches_dataframes)