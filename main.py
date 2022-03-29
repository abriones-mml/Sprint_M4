from limpiarconsola import *
from clase_usuario import Usuario
from clase_operario import Operario
from clase_administrador import Administrador
from clase_bodega import Bodega
from clase_proveedor import Proveedor
from clase_producto import Producto

# Proveedores
tipo_producto = {1: "Tecnología", 2: "Calzado", 3: "Casa y Decoración", 4: "Deportes", 5: "Vestuario"}
pv1 = Proveedor(1, "Proveedor 1", tipo_producto[1])
pv2 = Proveedor(1, "Proveedor 2", tipo_producto[2])
pv3 = Proveedor(1, "Proveedor 3", tipo_producto[3])
pv4 = Proveedor(1, "Proveedor 4", tipo_producto[4])
pv5 = Proveedor(1, "Proveedor 5", tipo_producto[5])

# Productos
a1 = Producto("Smartphone X67", tipo_producto[1], 139000)
a2 = Producto("Zapatillas Vands", tipo_producto[2], 49000)
a3 = Producto("Sofa Cama", tipo_producto[3], 60000)
a4 = Producto("Camiseta Shile rumbo a Qatar 2022", tipo_producto[4], 9990)
a5 = Producto("Poleron Negro", tipo_producto[5], 14990)
productos= {1: a1, 2: a2, 3: a3, 4: a4, 5: a5}


# Bodegas
provb1 = {1:pv1, 2:pv2}
prodb1 = {1:a1, 2:a2}

provb2 = {1:pv3, 2:pv4}
prodb2 = {3:a3, 4:a4}

provb3 = {1:pv1, 3:pv3, 3:pv5}
prodb3 = {1:a1, 3:a3, 5:a5}

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

o1 = Operario(b1, "Elton", "Torron", 22022001, 2, 123)
o2 = Operario(b2, "Esteban", "Dido", 22022002, 2, 1234)
o3 = Operario(b2, "Giovanni", "Durán", 22022003, 2, 12345)
o4 = Operario(b3, "Toribio", "Jiménez", 22022004, 2, 123456)

a1 = Administrador(b1, "Giselle", "Saa", 12022001, 1, 1234)
a2 = Administrador(b2, "Elza", "Pallo", 12022002, 1, 12345)
a3 = Administrador(b3, "Ivette", "Farías", 12022002, 1, 123456)

administradores = {1: a1, 2: a2, 3: a3}
operarios = {1: o1, 2: o2, 3: o3, 4: o4}

print(b1.productos[1].nombre, b1.stock["1"])
print(b3.productos[1].nombre)
b1.transferir_productos("1", 7, b3)
#b1.productos[1].stock-=1
print(b1.stock)
print(b3.stock)
print(b1.cont)
print(b3.cont)
print()
print()




"""
while True:
    limpiar()
    print("Acceso de usuario:\n")
    print("[1] Administrador.")
    print("[2] Operario.")
    print("[3] Salir.")
    
    opcion = int(input("\nSeleccione tipo de usuario: "))
    
    if opcion == 1:
        limpiar()
        intentos = 0
        maxintentos = 3
        salir = 0
        while True:
            try:
                n = int(input("Ingrese su contraseña (de momento se accede ingresando 1, 2 o 3 (3 bodegas 1 adm por bodega)):\t"))
                intentos += 1
                if administradores.get(n) != None:
                    break
            except: 
                print("Ingrese una contraseña de administrador válida!!")
                intentos += 1
            if intentos == maxintentos:
                salir = 1
                break
        if salir == 1:
            print("\nMáximo de intentos, por seguridad el programa se cerrará...")
            input()
            break
        else:
            while True:
                limpiar()
                print(f"Bienvenido Sr(a). administrador(a) de la bodega {administradores[n].bodega.id}: {administradores[n].nombre} {administradores[n].apellido}, ¿Qué desea hacer?\n ")
                print("[1] Gestión de Bodegas.")
                print("[2] Gestión de Proveedores.")
                print("[3] Salir")
                
                opcion = int(input("\nSeleccione opción: "))
                
                if opcion == 1:
                    limpiar()
                    print(">>>>>> Bodegas <<<<<<\n")
                    print(f"[1] Ver información de la bodega \"{administradores[n].bodega.nombre}\".")
                    print(f"[2] Agregar proveedor a \"{administradores[n].bodega.nombre}\".")
                    print(f"[3] Eliminar provedor de \"{administradores[n].bodega.nombre}\".")
                    print(f"[4] Transferir productos desde \"{administradores[n].bodega.nombre}\" a otra bodega.")
                    print(f"[5] Ver detalles de productos transferidos desde \"{administradores[n].bodega.nombre}\" a otras bodegas.")
                    print(f"[6] Volver a Menú anterior.")
                    
                    opcion1 = int(input("\nSeleccione opción: "))
                    
                    if opcion1 == 1:
                        pass
                    elif opcion1 == 2:
                        pass
                    elif opcion1 == 3:
                        pass
                    elif opcion1 == 4:
                        pass
                    elif opcion1 == 5:
                        pass
                    elif opcion1 == 6:
                        break
                    
                elif opcion == 2:
                    limpiar()
                    print(">>>>>> Proveedores <<<<<<")
                    print("[1] Ver proveedores y stock de productos por bodegas.")
                    print("[2] Volver.")
                    
                    opcion2 == int(input("\nSeleccione opción: "))
                    
                    if opcion2 == 1:
                        pass
                    elif opcion2 == 2:
                        break
                    
                elif opcion == 3:
                    break            
            
    if opcion == 2:

        limpiar()
        intentos = 0
        maxintentos = 3
        salir = 0
        while True:
            try:
                n = int(input("Ingrese su contraseña (de momento se ingresa con 1, 2, 3 o 4 ( 4 operarios y 3 bodegas, 1 en la b1, 2 en la b2 y 1 en la b3)):\t"))
                intentos += 1
                if operarios.get(n) != None:
                    break
            except: 
                print("Ingrese una contraseña de operario válida!!")
                intentos += 1
            if intentos == maxintentos:
                salir = 1
                break
        if salir == 1:
            print("\nMáximo de intentos, por seguridad el programa se cerrará...")
            input()
            break
        else:
            while True:
                limpiar()
                print(f"Bienvenido Sr(a). operario(a) de la bodega {operarios[n].bodega.id}: {operarios[n].nombre} {operarios[n].apellido}, ¿Qué desea hacer?\n ")
                print("[1] Consultar número de proveedores por bodega.")
                print("[2] Salir")
                
                opcion = int(input("\nSeleccione opción: "))
                
                if opcion == 1:
                    pass
                    
                elif opcion == 2:
                    break 
    if opcion == 3:
        break
    """
print("\nAdios!.")



"""
limpiar()
n = int(input("Ingrese contraseña: "))
# agregar excepciones, tal que no se caiga el programa si se mete un password incorrecta.

print(f"Buen día {usuarios[n].nombre} {usuarios[n].apellido}, qué desea hacer?\n")
input()

while True:
    limpiar()
    print(">>>>>> Menú Principal <<<<<<\n")
    print("[1] Bodegas.")
    print("[2] Proveedores.")
    print("[3] Salir:")



limpiar()
print("Que tenga buena jornada!\n")

"""