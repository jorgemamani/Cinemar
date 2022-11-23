class Sala():
    def __init__(self, numeroSala, capacidad, tipo, fecha, id_funcion):
        self._numeroSala: numeroSala
        self._capacidad: capacidad
        self._tipo: tipo
        

    @property
    def numeroSala(self):
        return self._numeroSala
    @property
    def capacidad(self):
        return self._capacidad
    @property
    def tipo(self):
        return self._tipo

    @numeroSala.setter
    def numeroSala(self, numeroSala):
        self._numeroSala = numeroSala
    
    @capacidad.setter
    def capacidad(self, capacidad):
        self._capacidad = capacidad

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

