class Reserva():
    def __init__(self, tituloPelicula, fecha, horario, sala, butaca, precio):
        self._tituloPelicula: tituloPelicula
        self._fecha: fecha
        self._horario: horario
        self._sala: sala
        self._butaca: butaca
        self._precio: precio

    @property
    def tituloPelicula(self):
        return self._tituloPelicula

    @property
    def fecha(self):
        return self._fecha

    @property
    def horario(self):
        return self._horario

    @property
    def sala(self):
        return self._sala

    @property
    def butaca(self):
        return self._butaca

    @property
    def precio(self):
        return self._precio

    @tituloPelicula.setter
    def tituloPelicula(self, tituloPelicula):
        self._tituloPelicula = tituloPelicula
    
    @fecha.setter
    def fecha(self, fecha):
        self._fecha = fecha

    @horario.setter
    def horario(self, horario):
        self._horario = horario

    @sala.setter
    def sala(self, sala):
        self._sala = sala

    @butaca.setter
    def butaca(self, butaca):
        self._butaca = butaca

    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
    