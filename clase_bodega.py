class Bodega:
    
    def __init__(self, id, nombre, __total_productos, proveedores, productos, stock, cont=0):
        #trans={}
        self.id = id
        self.nombre = nombre
        self.__total_productos = __total_productos
        self.proveedores = proveedores
        self.productos = productos
        self.stock = stock
        self.cont=cont

    def transferir_productos(self, producto_elegido, cantidad, destino):
        
        if self.stock[producto_elegido] >= cantidad and producto_elegido in destino.stock: # Si stock que se manda es mayor que la cantidad escogida
                                                                                            # y si el producto se encuentra en el stock del destino
            print(f"Producto transferido a {destino.nombre}")
            self.stock[producto_elegido] -= cantidad
            destino.stock[producto_elegido] += destino.stock[producto_elegido]
            print(f"El nuevo stock del producto en {self.nombre} es de {self.stock[producto_elegido]} unidad(es).")
            print(f"El nuevo stock del producto en {destino.nombre} es de {destino.stock[producto_elegido]} unidad(es).")       
            self.cont += cantidad

        elif self.stock[producto_elegido] >= cantidad and producto_elegido not in destino.stock: # Si stock del prodcuto a ebciar es mayor q sto
            destino.stock.update({producto_elegido:cantidad})
            self.stock[producto_elegido] -= cantidad
            self.cont+=cantidad
        
        else: 
            print(f"Despacho rechazado, no hay suficiente stock en {self.nombre}")  #cambiar this print


    def add_stock(self, ):
        pass


    def cant_prod_trans(self):
        pass
    
    def mostrar_tipos_trans(self):
        pass
    
    def mostrar_productos(self):
        pass


    def agregar_proveedor(self, dict_proveedores):
        for i in dict_proveedores:
            if self.proveedores.get(i) != None:
                pass
            else: print(dict_proveedores[i])
        p = int(input("\nSeleccione Proveedor a agregar: "))
        aux = dict_proveedores[p]
        self.proveedores[p] = aux
    
    def eliminar_proveedor(self):
        for i in self.proveedores:
            print(self.proveedores[i])
        p = int(input("\nSeleccione Proveedor a eliminar: "))
        del self.proveedores[p]
        # aqui se puedes agregar excepciones ;)
    
