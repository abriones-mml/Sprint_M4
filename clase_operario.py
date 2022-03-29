from clase_usuario import Usuario

class Operario (Usuario):
    
    def __init__(self, bodega, nombre, apellido, nid, rango, clave ):
        super().__init__(nombre, apellido, nid, rango, clave)
        self.bodega = bodega
        
    
    def proveedores_por_bodega(self):
        pass