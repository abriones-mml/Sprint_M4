class Proveedor:
    
    def __init__(self, id, nombre, tipo_producto):
        self.id = id
        self.nombre = nombre
        self.tipo_producto = tipo_producto
        
    def inscripcion_en_bodega(self, bodega):
        pass
    
    def modificar_tipo(self):
        pass
    
    def __str__(self):
        return '{:<5}{:<15}{:<20}'.format(self.id, self.nombre, self.tipo_producto)