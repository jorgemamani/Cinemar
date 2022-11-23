class Funcion():
    def __init__(self, horario, Sala, precio, fecha, id_funcion):
        self._horario: horario
        self._Sala: Sala
        self._precio: precio
        self._fecha: fecha
        self._id_funcion: id_funcion

    @property
    def horario(self):
        return self._horario
    @property
    def Sala(self):
        return self._Sala
    @property
    def precio(self):
        return self._precio
    @property
    def fecha(self):
        return self._fecha
    @property
    def id_funcion(self):
        return self._id_funcion

    @horario.setter
    def horario(self, horario):
        self._horario = horario

    @Sala.setter
    def Sala(self, Sala):
        self._Sala = Sala

    @precio.setter
    def precio(self, precio):
        self._precio = precio

    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha
        
    @id_funcion.setter
    def id_funcion(self, id_funcion):
        self._id_funcion = id_funcion

