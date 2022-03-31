class Producto:
    
    def __init__(self, nombre, tipo, precio):
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
   #Método para obtener en pantalla un string con los datos del producto 
    def __str__(self):
        return '{:<30}{:<15}{:<15}'.format(self.nombre, self.tipo, self.precio)
    def mostrar_productos():
        print("Los productos en nuestra bodega son los siguientes: \n\n"  '{:<30}{:<15}{:<15}'.format("Nombre", "Tipo", "Precio"))
        print(("*"*70))
        for key in productos:
            print(productos[key])
            input()
