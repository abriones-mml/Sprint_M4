class Proveedor:
    
    def __init__(self, id, nombre, tipo_producto):
        self.id = id
        self.nombre = nombre
        self.tipo_producto = tipo_producto
        
    def __str__(self):
        return '{:<5}{:<15}{:<20}'.format(self.id, self.nombre, self.tipo_producto)
    
    def mostrar_proveedores():
        print("Los proveedores registrados son los siguientes: \n\n"  '{:<5}{:<15}{:<20}'.format("Id", "Nombre", "Tipo de Productos"))
        print(("*"*45))
        for i in prov:
            print(i)
        input()
    
    def modificar_tipo(tipo_producto):
        cambiar_tipo=int(input("Seleccione al proveedor que desea modificar el tipo de producto: "))-1
        print(f"El tipo de producto del proveedor es :{tipo_producto[cambiar_tipo]}")
        nuevo_tipo=input("Indique cual es la nueva categoria del producto: ").title()
        tipo_producto[cambiar_tipo].tipo_producto= nuevo_tipo
        print("El tipo de producto se ha cambiado exitosamente")
        print(f"El nuevo tipo del producto es: {tipo_producto[cambiar_tipo]}")

    def agregar_proveedor():
        id=int(input("Indique el numero de id: "))
        nombre=input("Agregue nombre del proveedor: ").title()
        tipo= input("Agregue la categoria del producto: ").title()
        tipo_producto[id]=tipo
        tipo_producto
        pv=Proveedor(id, nombre,tipo)
        prov.append(pv)
        print("A cuál bodega desea agregar el proveedor: ")
        print("1 : bodega 1  ""2 : bodega 2  " "3 : bodega3")
        bodega_elegida=input("Nombre de bodega elegida: ")
        bodegaprov[bodega_elegida].append(pv)

    def eliminar_proveedor():
        id_eliminar=int(input("Seleccione el ID del proveedor que quiere eliminar: "))
        del prov[id_eliminar - 1]
        Proveedor.mostrar_proveedores()
        print("El Proveedor se ha eliminado exitosamente")

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

    def __str__(self):
        return f"Datos Bodega son :"'{:<15}{:<15}{:<15}{:<15}{:<15}'.format(self.id, self.nombre, self.__total_productos, self.proveedores, self.productos)
    def mostrar_bodega( ):
        print("Los productos en nuestra bodega son los siguientes: \n\n"  '{:<30}{:<15}{:<15}'.format("Id", "Nombre", "Total de productos", "proveedores", "productos"))
        print(("*"*70))
        for i in bodegas:
            print(i)
            input()

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
    
# Proveedores
tipo_producto = {1: "Tecnología", 2: "Calzado", 3: "Casa y Decoración", 4: "Deportes", 5: "Vestuario"}
pv1 = Proveedor(1, "Proveedor 1", tipo_producto[1])
pv2 = Proveedor(2, "Proveedor 2", tipo_producto[2])
pv3 = Proveedor(3, "Proveedor 3", tipo_producto[3])
pv4 = Proveedor(4, "Proveedor 4", tipo_producto[4])
pv5 = Proveedor(5, "Proveedor 5", tipo_producto[5])

a1 = Producto("Smartphone X67", tipo_producto[1], 139000)
a2 = Producto("Zapatillas Vands", tipo_producto[2], 49000)
a3 = Producto("Sofa Cama", tipo_producto[3], 60000)
a4 = Producto("Camiseta Shile rumbo a Qatar 2022", tipo_producto[4], 9990)
a5 = Producto("Poleron Negro", tipo_producto[5], 14990)
productos= {1: a1, 2: a2, 3: a3, 4: a4, 5: a5}

prov=[pv1, pv2, pv3, pv4, pv5]

provb1 = [pv1, pv2]

provb2 = [pv3, pv4]
provb3 = [pv1, pv3, pv5]

prodb1 = {1:a1, 2:a2}

prodb2 = {3:a3, 4:a4}

prodb3 = {1:a1, 3:a3, 5:a5}   


bodegaprov={"1": provb1, "2":provb2, "3":provb3}




a={"1":1000,"2":1000}
b={ "3":1, 
    "4":2, 
        }
c={
    "1":7,
    
    "3":7, 
   
    "5":7
    }
b1 = Bodega(1, "Bodega 1", 1000, provb1, prodb1, a)
b2 = Bodega(2, "Bodega 2", 1000, provb2, prodb2, b)
b3 = Bodega(3, "Bodega 3", 1000, provb3, prodb3, c)
bodegas=[b1, b2, b3]
print(tipo_producto.keys())
Proveedor.mostrar_proveedores()
print(Proveedor.__str__(pv2))


Proveedor.agregar_proveedor()
print(prov[-1].nombre)
print(prov[-1].tipo_producto)
print(tipo_producto.keys())

for i in provb3:
    print(i)
print("\n")

for i in provb1:
    print(i)

print("\n")

for i in provb2:
    print(i)

print("\n")

for i in provb3:
    print(i)



Proveedor.modificar_tipo(prov)
Proveedor.mostrar_proveedores()
