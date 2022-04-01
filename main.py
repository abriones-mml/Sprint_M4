from limpiarconsola import *
from datos import *

"""
print(b1.productos[1].nombre, b1.stock[1])
print(b3.productos[1].nombre)
b1.transferir_productos(1, 7, b2)
#b1.productos[1].stock-=1
print(b1.stock)
print(b2.stock)
print(b1.cont)
print(b2.cont)
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
                    
                    # 1.1 Info de la bodega
                    if opcion1 == 1:
                        limpiar()
                        print(f">>> Información {administradores[n].bodega.nombre} <<<\n")
                        print("Proveedores de Bodega:") 
                        for i in administradores[n].bodega.proveedores:
                            print(f"\t\t\t- {administradores[n].bodega.proveedores[i].nombre}")
                        print("\nAquí se debería desplegar el detalle de los productos (NOMBRE, PRECIO (si es que lo agregamos), STOCK, PROVEEDOR")
                        input()
                    
                    # 1.2 Agregar proveedor a bodega
                    elif opcion1 == 2:
                        limpiar()
                        print(f">>> Agregar Proveedor a {administradores[n].bodega.nombre} <<<\n")
                        print("{:<5}{:<15}{:<20}".format("ID", "Nombre", "Tipo de Producto"))
                        print("="*40)
                        administradores[n].bodega.agregar_proveedor(proveedores)
                        input()
                        
                    # 1.3 Eliminar proveedor existente en bodega
                    elif opcion1 == 3:
                        limpiar()
                        print(f">>> Eliminar Proveedor de {administradores[n].bodega.nombre} <<<\n")
                        print("{:<5}{:<15}{:<20}".format("ID", "Nombre", "Tipo de Producto"))
                        print("="*40)
                        administradores[n].bodega.eliminar_proveedor()
                        input()
                    
                    # 1.4 Transferir productos a otra bodega.
                    elif opcion1 == 4:
                        limpiar()
                        print(f">>> Transferir Productos desde {administradores[n].bodega.nombre} <<<\n")
                        for i in bodegas:
                            if administradores[n].bodega != bodegas[i]:
                                print(f"[{bodegas[i].id}] {bodegas[i].nombre}")
                            else: pass
                            
                        b =  int(input("\nA qué Bodega desea transferir productos?: "))
                        
                        limpiar()
                        print(f"¿Qué producto desea transferir a {bodegas[b].nombre}?:\n")
                        for key in bodegas[n].productos:
                            print(f"[{key}]\t{productos[key].nombre}")
                        p = int(input("\Seleccione producto: "))
                        limpiar()
                        u = int(input(f"¿Cuántas unidades de {productos[p].nombre} desea enviar a la {bodegas[b].nombre}?: "))
                        bodegas[n].transferir_productos(p, 100, bodegas[b])
                        input()
                
                    # 1.5 Detalle de transferencias de productos
                    elif opcion1 == 5:
                        pass
                    
                    elif opcion1 == 6:
                        break
                    
                elif opcion == 2:
                    limpiar()
                    print(">>>>>> Proveedores <<<<<<")
                    print(f"[1] Ver proveedores y stock de productos en {administradores[n].bodega.nombre} .")
                    print("[2] Agregar Proveedor.")
                    print("[3] Eliminar Proveedor.")
                    print("[4] Modificar Tipo de producto ofrecido por un proveedor.")
                    print("[5] Volver Menú principal.")
                    
                    opcion2 = int(input("\nSeleccione opción: "))
                    
                    # 2.1 Ver proveedores (stock de momento no aparece)
                    if opcion2 == 1:
                        limpiar()
                        print(f">>> Proveedores de {administradores[n].bodega.nombre}  <<<\n")
                        print('{:<5}{:<15}{:<20}'.format("Id", "Nombre", "Tipo Producto"))
                        print("="*40)
                        for key in administradores[n].bodega.proveedores:
                            print(administradores[n].bodega.proveedores[key])
                        input()
                        
                    # 2.2 
                    elif opcion2 == 2:
                        pass
                    
                    # 2.3 Eliminar proveedor.
                    elif opcion2 == 3:
                        pass

                    # 2.4 Modificar tipo producto.
                    elif opcion2 == 4:
                        pass
                    
                    elif opcion2 == 5:
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
        
print("\nAdios!.")
#"""

#"""


limpiar()
print("Que tenga buena jornada!\n")

#"""