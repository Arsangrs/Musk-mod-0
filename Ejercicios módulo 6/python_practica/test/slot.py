from datetime import datetime, timedelta

class Slot:
    # Constructor
    '''def __init__(self):
        self.id = None             # Asignar id del vuelo
        self.fecha_inicial = None  # Asinar la llegada
        self.fecha_final = None    # Asignar el despegue
    # Asignar un vuelo al slot
    def asigna_vuelo(self, id_vuelo, fecha_llegada, fecha_despegue):
        # Normalizar fechas si vienen como string
        if isinstance(fecha_llegada, str):
            fecha_llegada = datetime.strptime(fecha_llegada, '%Y-%m-%d %H:%M:%S')
        if isinstance(fecha_despegue, str):
            fecha_despegue = datetime.strptime(fecha_despegue, '%Y-%m-%d %H:%M:%S')
        self.id_vuelo = id_vuelo
        self.llegada = fecha_llegada
        self.despegue = fecha_despegue

    # Comprobar si el slot está libre en un momento determinado
    def esta_libre_en(self, fecha):
        if self.llegada is None or self.despegue is None:
            return True
        return fecha >= self.despegue

    # Retornar la fecha en que el slot estará libre para asignar un vuelo
    def proximo_inicio_libre(self, fecha):
        if self.despegue is None or fecha >= self.despegue:
            return fecha
        return self.despegue'''
    def __init__(self):
        self.id_vuelo = None      # ID del vuelo asignado
        self.llegada = None       # Fecha y hora de llegada
        self.despegue = None      # Fecha y hora de despegue

    # Asignar un vuelo al slot
    def asigna_vuelo(self, id_vuelo, fecha_llegada, fecha_despegue):
        """Asigna un vuelo al slot y normaliza fechas si vienen como string."""
        self.id_vuelo = id_vuelo

        if isinstance(fecha_llegada, str):
            self.llegada = datetime.strptime(fecha_llegada, '%Y-%m-%d %H:%M:%S')
        else:
            self.llegada = fecha_llegada

        if isinstance(fecha_despegue, str):
            self.despegue = datetime.strptime(fecha_despegue, '%Y-%m-%d %H:%M:%S')
        else:
            self.despegue = fecha_despegue

    # Comprobar si el slot está libre en un momento dado
    def esta_libre_en(self, fecha):
        """Devuelve True si el slot está libre en la fecha indicada."""
        if self.llegada is None or self.despegue is None:
            return True
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        return fecha >= self.despegue

    # Retornar la fecha en que el slot estará libre
    def proximo_inicio_libre(self, fecha):
        """Devuelve la fecha más temprana en que el slot estará libre a partir de 'fecha'."""
        if self.despegue is None:
            return fecha
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d %H:%M:%S')
        return max(fecha, self.despegue)