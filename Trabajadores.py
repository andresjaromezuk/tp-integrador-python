from Personas import Persona

class Trabajador(Persona):
  def __init__(
      self, nombre_completo, fecha_nacimiento, genero, zipcode,
      posicion, categoria, horas_trabajo, fecha_ingreso, id = None):
    Persona.__init__(self, nombre_completo, fecha_nacimiento, genero, zipcode)
    self.posicion = posicion
    self.categoria = categoria
    self.horas_trabajo = horas_trabajo
    self.fecha_ingreso = fecha_ingreso
    self.id = id



