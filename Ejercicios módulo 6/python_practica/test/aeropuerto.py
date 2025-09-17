import pandas as pd
from datetime import timedelta
from slot import Slot

# Clase aeropuerto
class Aeropuerto:
    # Constructor
    def __init__(self, vuelos, slots, t_embarque_nat, t_embarque_internat):
        self.df_vuelos = vuelos.copy()
        self.n_slots = slots
        self.slots = {i: Slot() for i in range(1, slots + 1)}
        self.tiempo_embarque_nat = t_embarque_nat
        self.tiempo_embarque_internat = t_embarque_internat

        self.df_vuelos['fecha_despegue'] = pd.NaT
        self.df_vuelos['slot'] = 0

    # Calcular fecha despegue
    '''def calcula_fecha_despegue(self, row):
        if pd.isna(row['retraso']) or row['retraso'] == '-':
            retraso = timedelta()
        else:
            h, m = map(int, str(row['retraso']).split(':'))
            retraso = timedelta(hours=h, minutes=m)        
        tiempo_embarque = self.tiempo_embarque_nat if row['tipo_vuelo'].upper() == 'NAT' else self.tiempo_embarque_internat
        embarque_td = timedelta(minutes=tiempo_embarque)

        row['fecha_despegue'] = row['fecha_llegada'] + retraso + embarque_td
        return row'''
    
    def calcula_fecha_despegue(self, row):
        retraso = timedelta()
        if not pd.isna(row['retraso']) and row['retraso'] != '-':
            try:
                h, m = map(int, str(row['retraso']).split(':'))
                retraso = timedelta(hours=h, minutes=m)
            except Exception:
                print(f"⚠️ Formato de retraso inválido en vuelo {row.get('id', 'desconocido')}: {row['retraso']}")
                retraso = timedelta()

        tiempo_embarque = (
            self.tiempo_embarque_nat
            if row['tipo_vuelo'].upper() == 'NAT'
            else self.tiempo_embarque_internat
        )
        embarque_td = timedelta(minutes=tiempo_embarque)

        row['fecha_despegue'] = row['fecha_llegada'] + retraso + embarque_td
        return row


    # Buscar slot libre
    def encuentra_slot(self, fecha_vuelo):
        # Buscar un slot libre o buscar el primero que quede libre más tarde
        min_fecha = None
        slot_seleccionado = None
        # Recorrer los slots
        for numero, slot in self.slots.items():
            # Conmprobar si el slot está libre en la fecha del vuelo y si no, cuándo queda libre
            if slot.esta_libre_en(fecha_vuelo):
                return numero, fecha_vuelo
            else:
                proximo = slot.proximo_inicio_libre(fecha_vuelo)
                if min_fecha is None or proximo < min_fecha:
                    min_fecha = proximo
                    slot_seleccionado = numero
        # Si no hay slot libre, adjudicar el primero que quede libre
        return slot_seleccionado, min_fecha

    # Asignar slot a un vuelo
    def asigna_slot(self, vuelo):
        vuelo = self.calcula_fecha_despegue(vuelo)
        slot_libre, nueva_fecha = self.encuentra_slot(vuelo['fecha_despegue'])

        # Ajustar la fecha de llegada/despegue si hubo que esperar
        if nueva_fecha > vuelo['fecha_despegue']:
            diferencia = nueva_fecha - vuelo['fecha_despegue']
            vuelo['fecha_llegada'] += diferencia
            vuelo['fecha_despegue'] += diferencia
        # Asignar el slot
        vuelo['slot'] = slot_libre
        self.slots[slot_libre].asigna_vuelo(vuelo['id'], vuelo['fecha_llegada'], vuelo['fecha_despegue'])

        # Salida esperada por consola según video explicativo
        '''print(f"El vuelo {vuelo['id']} con fecha de llegada {vuelo['fecha_llegada']} "
              f"y despegue {vuelo['fecha_despegue']} ha sido asignado al slot {slot_libre}")'''

        return vuelo
    # Asignar slots a todos los vuelos
    def asigna_slots(self):
        self.df_vuelos = self.df_vuelos.apply(self.asigna_slot, axis=1)
        
    @staticmethod
    def preprocess_data(df_list):
        # Combinar dataframes
        df_combined = pd.concat(df_list, ignore_index=True)

        # Convertir "-" en NaT en columna 'retraso'
        if 'retraso' in df_combined.columns:
            df_combined['retraso'] = df_combined['retraso'].replace('-', pd.NaT)

        # Asegurar que 'fecha_llegada' es datetime
        if 'fecha_llegada' in df_combined.columns:
            df_combined['fecha_llegada'] = pd.to_datetime(
                df_combined['fecha_llegada'],
                errors='coerce',
                dayfirst=True
            )
        return df_combined