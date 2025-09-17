import os
import pandas as pd
from lector import LectorTXT, LectorCSV, LectorJSON
from aeropuerto import Aeropuerto
from vista_html import vista_html

# Combinar dataframes 
'''def preprocess_data(df_list):
    # Combinar dataframes
    df_combined = pd.concat(df_list, ignore_index=True)
    
    # Convertir "-" en NaT en columna 'retraso'
    if 'retraso' in df_combined.columns:
        df_combined['retraso'] = df_combined['retraso'].replace('-', pd.NaT)
    
    # Controlar que la 'fecha_llegada' es datetime
    if 'fecha_llegada' in df_combined.columns:
        df_combined['fecha_llegada'] = pd.to_datetime(df_combined['fecha_llegada'], errors='coerce', dayfirst=True)    
    return df_combined'''

if __name__ == '__main__':
    # Rutas a los archivos
    path_1 = os.path.abspath('./data/vuelos_1.txt')
    path_2 = os.path.abspath('./data/vuelos_2.csv')
    path_3 = os.path.abspath('./data/vuelos_3.json')

    # Leer los tres archivos
    lector_txt = LectorTXT(path_1)
    df_txt = lector_txt.lee_archivo()

    lector_csv = LectorCSV(path_2)
    df_csv = lector_csv.lee_archivo(datetime_columns=['fecha_llegada'])

    lector_json = LectorJSON(path_3)
    df_json = lector_json.lee_archivo()

    # Combinar todos los DataFrames
    df_vuelos = Aeropuerto.preprocess_data([df_txt, df_csv, df_json])

    # Crear aeropuerto con 3 slots y tiempos de embarque
    aeropuerto = Aeropuerto(df_vuelos, slots=3, t_embarque_nat=30, t_embarque_internat=50)

    # Asignar slots a todos los vuelos
    aeropuerto.asigna_slots()

    # Mostrar resultado final que se muestra en el video de la realización del proyecto   
    for _, vuelo in aeropuerto.df_vuelos.iterrows():
        print(
            f"El vuelo {vuelo['id']} con fecha de llegada {vuelo['fecha_llegada']} "
            f"y despegue {vuelo['fecha_despegue']} ha sido asignado al slot {vuelo['slot']}."
        )
    
    # Generar una vista HTML del resultado    
    vista_html(aeropuerto.df_vuelos)