class Bodega:
    
    def __init__(self, id, nombre, __total_productos, proveedores, productos, stock, cont=0):
        ttrans={}
        self.id = id
        self.nombre = nombre
        self.__total_productos = __total_productos
        self.proveedores = proveedores
        self.productos = productos
        self.stock = stock
        self.cont=cont
        self.ttrans=ttrans

    def transferir_productos(self, producto_elegido, cantidad, sucursal):
        
        if self.stock[producto_elegido] >= cantidad and producto_elegido in sucursal.stock:
            print(f"Producto transferido a {sucursal.nombre}")
            self.stock[producto_elegido] = self.stock[producto_elegido]-cantidad
            sucursal.stock[producto_elegido] = sucursal.stock[producto_elegido]+cantidad
            print(f"El nuevo stock del producto en {self.nombre} es de {self.stock[producto_elegido]} unidad(es).")
            print(f"El nuevo stock del producto en {sucursal.nombre} es de {sucursal.stock[producto_elegido]} unidad(es).")       
            self.cont+=cantidad
            
            if producto_elegido not in self.ttrans:
                self.ttrans.update({producto_elegido:cantidad})
            else:
                self.ttrans[producto_elegido]=self.ttrans[producto_elegido]+cantidad
                        
        elif self.stock[producto_elegido] >= cantidad and producto_elegido not in sucursal.stock:
            sucursal.stock.update({producto_elegido:cantidad})
            self.stock[producto_elegido] = self.stock[producto_elegido]-cantidad
            self.cont+=cantidad

            if producto_elegido not in self.ttrans:
                self.ttrans.update({producto_elegido:cantidad})
            else:
                self.ttrans[producto_elegido]=self.ttrans[producto_elegido]+cantidad
        
        else: 
            print(f"Despacho rechazado, no hay suficiente stock en {self.nombre}")  #cambiar this print
        return self.ttrans

    def transferencias(self, productos_transferidos):
        print(f">>> Detalle de transferencias de productos desde {self.nombre}.\n")
        if productos_transferidos != []:
            print("{:10}{:40}{:20}".format("Unidades", "Producto", "Destino"))
            print("="*60)
            for i in range(len(productos_transferidos)):
                print("{:<10}{:40}{:20}".format(productos_transferidos[i][0], productos_transferidos[i][1], productos_transferidos[i][2]))
            self.mostrar_total_tipos_trans()
            self.mostrar_total_trans()
        else:
            print("Aún no se realizan transferencias de productos.")
    
    def total_bodega(self):
        total= sum(self.stock.values())
        self.__total_productos=total
        print(f"\nEn {self.nombre} hay un total de {self.__total_productos} unidades de productos.")
        
    def mostrar_total_tipos_trans(self):
        total = len(self.ttrans)
        print(f"\nDesde {self.nombre} se ha(n) transferido un total de {total} tipo(s) de producto(s) a otras bodegas.")
    
    def mostrar_total_trans(self):
        total = sum(self.ttrans.values())
        print(f"\nDesde {self.nombre} se ha(n) transferido un total de {total} unidad(es) de producto(s) a otras bodegas.")

    def agregar_proveedor(self, dict_proveedores):
        print(f">>> Agregar Proveedor a {self.nombre} <<<\n")
        print("{:<5}{:<15}{:<20}".format("ID", "Nombre", "Tipo de Producto"))
        print("="*40)
        for i in dict_proveedores:
            if self.proveedores.get(i) != None:
                pass
            else: print(dict_proveedores[i])
        p = int(input("\nSeleccione Proveedor a agregar: "))
        aux = dict_proveedores[p]
        self.proveedores[p] = aux
    
    def eliminar_proveedor(self):
        print(f">>> Eliminar Proveedor de {self.nombre} <<<\n")
        print("{:<5}{:<15}{:<20}".format("ID", "Nombre", "Tipo de Producto"))
        print("="*40)
        for i in self.proveedores:
            print(self.proveedores[i])
        p = int(input("\nSeleccione Proveedor a eliminar: "))
        del self.proveedores[p]
        # aqui se puedes agregar excepciones ;)
        
        
    def infobodega(self, stock_en_bodega):
        print(f">>> Información {self.nombre} <<<\n")
        print("Proveedores de Bodega:") 
        for i in self.proveedores:
            print(f"\t\t\t- {self.proveedores[i].nombre}")
        print("\nDetalle de Productos en Bodega:\n")
        print("{:38}{:12}{:15}{:>6}{:>18}".format("Nombre", "Precio", "Stock", "Categoría", "Proveedor"))
        print("="*95)
        for i in self.productos:
            print("{:34}{:9}{:10}{:>20}{:>20}".format(self.productos[i].nombre, self.productos[i].precio, stock_en_bodega[i], self.productos[i].proveedor.tipo_producto, self.productos[i].proveedor.nombre))