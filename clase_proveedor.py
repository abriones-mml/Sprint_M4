class Proveedor:
    
    def __init__(self, id, nombre, tipo_producto):
        self.id = id
        self.nombre = nombre
        self.tipo_producto = tipo_producto
        
    def inscripcion_en_bodega(self, bodega, dict_proveedores):
        bodega.proveedores[self.id] = dict_proveedores[self.id]
        print(f"El proveedor {self.nombre} ha sido inscrito en {bodega.nombre}")
    
    def modificar_tipo(self, tipo_anterior):
        t = input(f"Ingrese el nuevo tipo de producto del proveedor {self.nombre}:  ").title()
        self.tipo_producto = t
        print(f"El tipo de producto del proveedor {self.nombre} ha cambiado de {tipo_anterior} a {self.tipo_producto}.")

    
    def __str__(self):
        return '{:<5}{:<15}{:<20}'.format(self.id, self.nombre, self.tipo_producto)