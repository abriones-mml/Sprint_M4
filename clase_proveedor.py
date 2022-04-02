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
    
    
     def modificar_tipo(self, tipo_producto):
        cambiar_tipo=int(input("Seleccione al proveedor que desea modificar el tipo de producto: "))-1
        print(f"El tipo de producto del proveedor es :{self[cambiar_tipo].tipo_producto}")
        nuevo_tipo=input("Indique cual es la nueva categoria del producto: ").title()
        self[cambiar_tipo].tipo_producto= nuevo_tipo
        print("El tipo de producto se ha cambiado exitosamente")
        print(f"El nuevo tipo del producto es: {self[cambiar_tipo].tipo_producto}")


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
