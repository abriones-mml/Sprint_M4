class Producto:
    
    def __init__(self, nombre, proveedor, precio):
        self.nombre = nombre
        self.proveedor = proveedor
        self.precio = precio
    
    def mostrar(self, stocks):
        for i in self.productos: # DRAMON para mostrar stock de prodcutos.
            print("{:25}{:10}{:10}{:15}{:10}".format(self.nombre[i], self.stock[i], self.precio[i], self.proveedor[i], stocks))
