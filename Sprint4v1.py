#La clase Bodega la cual tendrá los siguientes atributos: 
# ● Id ● Nombre ● __Cantidad total de productos ● Proveedores ( lista de objetos proveedores ) 
# ● Un dato con los productos y su respectivo stock Y también deberá contar con los siguientes métodos:
#  ● Agregar_proveedor ● Eliminar_proveedor ● Transferir productos de una bodega a otra bodega. 
# ● Cantidad total de productos transferidos. ● Mostrar total de tipos de productos transferidos. 
# ● Mostrar total de productos en bodega. 
# La clase Proveedor tendrá los siguientes atributos: ● ID ● Nombre ● Tipo de productos que ofrece 
# Y también los siguientes métodos: ● Inscripción en bodega ● Modificar el tipo de producto ofrecido. 
# Cada Bodega tiene operarios y administradores. Ambos comparten la capacidad de consultar el número de proveedores por bodega. 
# Los administradores tienen la capacidad de conocer el número de proveedores por bodega y el stock.
#Agregue aplicaciones prácticas de los métodos creados en el ejercicio. Recomendamos dividir el ejercicio entre los integrantes del equipo. Consideraciones generales
#Creación de la clase Usuario

class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre=nombre
        self.__contraseña=contraseña

    
#Creación de las clases Operarios y Administrador que heredan de Usuario

class Operarios(Usuario):
    pass
#Consultar proveedores
class Administrador(Usuario):
    pass
#Consultar provedores, bodega y stock


#Creación de la clase Bodega

class Bodega:
    def __init__(self, id, nombre, cantidad_productos, proveedores, productos, contador=0):
        self.id= id
        self.nombre= nombre
        self.__cantidad_productos=cantidad_productos
        self.proveedores=proveedores
        self.productos=productos
        self.contador= contador

    def despachar_producto(self, producto_elegido, cantidad, contador):
        if self.__cantidad_productos[producto_elegido]>=cantidad:
            print("Producto despachado a sucursal")
            self.__cantidad_productos[producto_elegido]=self.__cantidad_productos[producto_elegido]-cantidad
            sucursal.stock[producto_elegido]=sucursal.stock[producto_elegido]+cantidad
            print(f"El nuevo stock es de {a.stock[producto_elegido]} unidad(es).")
        else: 
            print("Compra Rechazada, no queda stock")
    def recepcionar_producto(producto_elegido, cantidad):
        if sum(a.stock.values())<500:
            a.stock[producto_elegido]=a.stock[producto_elegido]+cantidad
            print("Producto recepcionado")
        else: print("Producto despachado, limite de stock")
    def __str__(self):
        return f"Datos Bodega principal:"'{:<15}{:<15}'.format(self.direccion, self.mt2)
    def mostrar_stock():
        for key in a.stock:
            print(key, a.stock[key])
            input()
#Creación de sucursal
class Sucursal(Bodega):
    pass

    #Crear metodos: 1. Agregar proveedor
                #   2. ELiminar proveedor
                #   3. Transferir productos bodega: despacho productos, recepcion de productos como el ABP4.
                #   4. Total productos despachados de bodega.
                #   5. Total por tipo de productos
                #   6. Total productos bodega(sum (productos.stock))

#Creación de la clase Productos 
class Productos:
    def __init__(self, sku, nombre, categoria, proveedores, stock):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedores= proveedores
        self.stock= stock
#Método para obtener en pantalla un string con los datos del producto 
    def __str__(self):
        return '{:<10}{:<15}{:<15}{:<15}{:<10}'.format(self.sku, self.nombre, self.categoria, self.proveedores, self.stock)
    def mostrar_productos():
        print("Los productos en nuestra bodega son los siguientes: \n\n"  '{:<10}{:<15}{:<15}{:<15}{:<10}'.format("Sku", "Nombre", "Categoria", "Proveedores", "Stock"))
        print(("*"*65))
        for key in productos:
            print(productos[key])
            input()
    def categoria_producto(self, modificar_producto, categoria):
        Productos.mostrar_productos()
        self.categoria[modificar_producto]=categoria
        
#Instancias de productos
zapatillas= Productos(20221, "zapatillas", "calzado", "Adidas_SA", 50)
jeans= Productos(20222, "jeans", "vestuario","Foster_SA", 30)
audifonos= Productos(20223, "audifonos", "electronica", "Phillips_SA", 20)
chocolates= Productos(20224, "chocolate", "alimentacion", "Costa", 40)
vino= Productos(20225, "Vino 1.5L","licores", "Gato", 35)

#Creación de un diccionario con los objetos productos
productos= {"1":zapatillas, "2":jeans, "3":audifonos, "4":chocolates, "5":vino}

#Creación de un diccionario con los objetos productos
productos= {"1":zapatillas, "2":jeans, "3":audifonos, "4":chocolates, "5":vino}

# Creación de la clase Proveedor
class Proveedor:
    def __init__(self, id, nombre, productos):
        self.id= id
        self.nombre= nombre
        self.productos=productos

    #Crear métodos: 1. Inscripción de Bodega
                #   2. Modificar tipo de producto.
    def modificar_producto(self, modificar_producto):
        print(self.productos[modificar_producto])
    #Método para obtener en pantalla un string con los datos del proveedor   
    def __str__(self):
        return '{:<15}{:<15}{:<20}'.format(self.id, self.nombre, self.productos)
    def mostrar_proveedores():
        print("Los proveedores registrados son los siguientes: \n\n"  '{:<15}{:<15}{:<20}'.format("Id", "Nombre", "Tipo de Productos"))
        print(("*"*55))
        for key in proveedores:
            print(proveedores[key])
            input()

#Creacion de objetos de proveedores
prov1= Proveedor("72635988-7", "Adidas_SA", productos["1"].categoria)
prov2= Proveedor("66359188-7", "Foster_SA", productos["2"].categoria)
prov3= Proveedor("75635988-8", "Phillips_sa", productos["3"].categoria)
prov4= Proveedor("69635988-3", "Costa", productos["4"].categoria)
prov5= Proveedor("77635988-5", "Gato", productos["5"].categoria)

#Creación de un diccionario con los objetos proveedores
proveedores={"1":prov1, "2":prov2, "3":prov3, "4":prov4, "5":prov5}
#Menú para acceder a la base de datos de Te lo vendo
while True:
    print("\n-----Bienvenido a Te lo vendo Market-----\n")
    print("[1] Operarios.")
    print("[2] Administrativos")
    print("[3] Salir")
    opcion1 = int(input("Seleccione una opción: "))        
    if opcion1== 1:
        while True:
            print("\n-----Bienvenidos operarios a Te lo vendo Market-----\n")        
            print("[1] Mostrar proveedores.")
            print("[2] Salir")
            opcion2 = int(input("Seleccione una opción: "))
            if opcion2 == 1:
                Proveedor.mostrar_proveedores()
            elif opcion2 == 2:
                break
    elif opcion1==2:
        while True:
            print("\n-----Bienvenido Administrador a Te lo vendo Market-----\n")        
            print("[1] Mostrar proveedores.")
            print("[2] Acceder a bodega")
            print("[3] Salir")
            opcion2 = int(input("Seleccione una opción: "))
            if opcion2 == 1:
                Proveedor.mostrar_proveedores()
            elif opcion2 == 2:
                while True:
                    print("\n-----Bodega de Te lo vendo Market-----\n")        
                    print("[1] Agregar proveedor.")
                    print("[2] Eliminar proveedor")
                    print("[3] Ver stock de productos bodega")
                    print("[4] Modificar producto")
                    print("[5] Salir")
                    opcion3 = int(input("Seleccione una opción: "))
                    if opcion3 ==1:
                        break
                    elif opcion3 ==2:
                        break
                    elif opcion3 ==3:
                        break
                    elif opcion3 ==4:
                        modificar_producto=input("Cual producto deses cambiar, digite 1-5: ")
                        categoria= input("Escriba la nueva categoria del producto: ")
                        Productos.categoria_producto(modificar_producto, categoria)
                        Proveedor.modificar_producto(modificar_producto)
                    elif opcion3 ==5:
                        break
            elif opcion2 ==3:
                break
    elif opcion1 ==3:
        print("\n Que tenga un buen día")
        break
