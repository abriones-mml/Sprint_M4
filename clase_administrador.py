from clase_operario import Operario

class Administrador(Operario):
    
    def __init__(self, bodega, nombre, apellido, nid, rango, clave ):
        super().__init__(bodega, nombre, apellido, nid, rango, clave)
