import pandas as pd
import json
import os

# Clase lector
class Lector:
    # Constructor
    def __init__(self, path: str):
        self.path = path
        self._comprueba_extension(self.ext)
    ext = ''
    # Manejar la extensión del archivo y marcar error si no es correcta
    def _comprueba_extension(self, extension):
        # Comprobar que el archivo existe
        if not os.path.isfile(self.path):
            raise FileNotFoundError(f"El archivo '{self.path}' no existe.")
        # Comprobar la extensión
        if not self.path.lower().endswith(extension):
            raise ValueError(f"El archivo debe tener extensión {extension}.")
    # Leer el archivo
    def lee_archivo(self):
        raise NotImplementedError("Este método debe ser implementado en la subclase")
    # Convertir el diccionario a DataFrame
    @staticmethod
    def convierte_dict_a_csv(data: dict):
        return pd.DataFrame(data)
    @staticmethod
    def convierte_columnas_fecha(df, columns):
        # Convierte las columnas indicadas a datetime de forma segura
        for col in columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col].astype(str).str.replace('T', ' '), 
                                         format='%d/%m/%Y %H:%M', errors='coerce')
        return df
# Clase para lector CSV
class LectorCSV(Lector):
    '''# Constructor
    def __init__(self, path: str):
        super().__init__(path)
        self._comprueba_extension('.csv')
    # Leer el archivo CSV y convertir columnas de fecha si es necesario y devolver DataFrame
    def lee_archivo(self, datetime_columns=[]):
        df = pd.read_csv(self.path, skipinitialspace=True)
        for col in datetime_columns:
            if col in df.columns:
                df[col] = pd.to_datetime(df[col], format='%d/%m/%Y %H:%M', errors='coerce')
        return df'''
    ext = '.csv'

    def lee_archivo(self, datetime_columns=[]):
        df = pd.read_csv(self.path, skipinitialspace=True)
        df = self.convierte_columnas_fecha(df, datetime_columns)
        return df
# Clase para lector JSON
class LectorJSON(Lector):
    '''# Constructor
    def __init__(self, path: str):
        super().__init__(path)
        self._comprueba_extension('.json')
    # Leer el archivo JSON y convertir a DataFrame
    def lee_archivo(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return self.convierte_dict_a_csv(data)'''
    ext = '.json'

    def lee_archivo(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return self.convierte_dict_a_csv(data)
# Clase para lector TXT
class LectorTXT(Lector):
    # Constructor
    '''def __init__(self, path: str):
        super().__init__(path)
        self._comprueba_extension('.txt')
    # Leer el archivo TXT y convertir a DataFrame
    def lee_archivo(self):
        df = pd.read_csv(self.path, skipinitialspace=True)
        if 'fecha_llegada' in df.columns:
            df['fecha_llegada'] = df['fecha_llegada'].str.replace('T', ' ')
            df['fecha_llegada'] = pd.to_datetime(df['fecha_llegada'], format='%d/%m/%Y %H:%M', errors='coerce')
        return df'''
    ext = '.txt'

    def lee_archivo(self):
        df = pd.read_csv(self.path, skipinitialspace=True)
        return self.convierte_columnas_fecha(df, ['fecha_llegada'])