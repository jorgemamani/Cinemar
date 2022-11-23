class Pelicula:
  def __init__(self,id,nombre,genero,duracion,descripcion,clasificacion,tipo,idioma):
    self.__id=id
    self.__nombre=nombre
    self.__genero = genero
    self.__duracion = duracion
    self.__descripcion=descripcion
    self.__clasificacion=clasificacion
    self.__tipo=tipo
    self.__idioma=idioma

  @property
  def id(self):
    return self.__id
  @property
  def nombre(self):
    return self.__nombre
  @property
  def genero(self):
    return self.__genero
  @property
  def duracion(self):
    return self.__duracion
  @property
  def descripcion(self):
    return self.__descripcion
  @property
  def clasificacion(self):
    return self.__clasificacion
  @property
  def tipo(self):
    return self.__tipo
  @property
  def idioma(self):
    return self.__idioma


  #def __str__(self):
  #  return f"\nDATOS:\nNombre: {self.__nombre}\nApellido: {self.__apellido}\nEdad: {self.__edad}\nDNI: {self.__dni}"
  
  def mostrar(self):
    return self.__nombre + "  " + self.__nombre + "  "