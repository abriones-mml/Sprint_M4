from limpiarconsola import *
from datos import *

while True:
    limpiar()
    print("Acceso de usuario:\n")
    print("[1] Administrador.")
    print("[2] Operario.")
    print("[3] Salir.")
    
    opcion0 = int(input("\nSeleccione tipo de usuario: "))
    
    if opcion0 == 1:
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
                
                # Menú de bodegas
                if opcion == 1:
                    limpiar()
                    print(">>>>>> Bodegas <<<<<<\n")
                    print(f"[1] Ver información de la bodega \"{administradores[n].bodega.nombre}\".")
                    print(f"[2] Agregar proveedor a \"{administradores[n].bodega.nombre}\".")
                    print(f"[3] Eliminar provedor de \"{administradores[n].bodega.nombre}\".")
                    print(f"[4] Transferir productos desde \"{administradores[n].bodega.nombre}\" a otra bodega.")
                    print(f"[5] Ver detalles de productos transferidos desde \"{administradores[n].bodega.nombre}\" a otras bodegas.")
                    print("[6] Ver información de todas las bodegas")
                    print("[7] Volver a Menú anterior.")
                    
                    opcion1 = int(input("\nSeleccione opción: "))
                    
                    # 1.1 Info de la bodega
                    if opcion1 == 1:
                        limpiar()
                        administradores[n].bodega.infobodega(stockes[n])
                        administradores[n].bodega.total_bodega()
                        input()
                    
                    # 1.2 Agregar proveedor a bodega
                    elif opcion1 == 2:
                        limpiar()
                        administradores[n].bodega.agregar_proveedor(proveedores)
                        input()
                        
                    # 1.3 Eliminar proveedor existente en bodega
                    elif opcion1 == 3:
                        limpiar()
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
                        p = int(input("\nSeleccione producto: "))
                        
                        limpiar()
                        u = int(input(f"¿Cuántas unidades de {productos[p].nombre} (stock: {administradores[n].bodega.stock[p]} unidades) desea enviar a la {bodegas[b].nombre}?: "))
                        transferencia = bodegas[n].transferir_productos(p, u, bodegas[b]) #devuelve diccionario de transferencias de bodega
                        
                        if transferencia:
                            transfer[n-1].append([u, administradores[n].bodega.productos[p].nombre, bodegas[b].nombre]) 
                        
                            idtrans = administradores[n].bodega.productos[p].proveedor.id
                        
                            if bodegas[b].proveedores.get(idtrans) != None:
                                print("El proveedor está inscrito en la bodega de destino")
                            else:
                                print("El proveedor no está inscrito en la bodega de destino")
                                bodegas[b].productos.update({p:productos[p]})
                                bodegas[b].proveedores[idtrans] = administradores[n].bodega.productos[p].proveedor
                                print(f"Proveedor {administradores[n].bodega.productos[p].proveedor.nombre} fue inscrito en {bodegas[b].nombre}")
                        input()
                
                    # 1.5 Detalle de transferencias de productos
                    elif opcion1 == 5:
                        limpiar()
                        administradores[n].bodega.transferencias(transfer[n-1])
                        input()
                        
                    # 1.6 Ver info de todas las bodegas.
                    elif opcion1 == 6:
                        limpiar()
                        print(">>> Información de Bodegas <<\n")
                        for i in bodegas:
                            print("="*80)
                            print(f"{bodegas[i].nombre}\n")
                            print("\tProveedores:")
                            for j in bodegas[i].proveedores:
                                print(f"\t\t► {bodegas[i].proveedores[j].nombre}")
                            print("\n\tProductos:")
                            for k in bodegas[i].productos:
                                print(f"\t\t► {bodegas[i].productos[k].nombre}\t{stockes[i][k]} unidades.")
                        input()
                    
                    # 1.7 Volver 
                    elif opcion1 == 7:
                        break
                    
                # Menú de proveedor
                elif opcion == 2:
                    limpiar()
                    print(">>>>>> Proveedores <<<<<<")
                    print(f"[1] Inscribir Proveedor en {administradores[n].bodega.nombre}.")
                    print(f"[2] Modificar Tipo de producto ofrecido por un proveedor en {administradores[n].bodega.nombre}.")
                    print("[3] Volver Menú principal.")
                    
                    opcion2 = int(input("\nSeleccione opción: "))
                    
                    # 2.1 Inscribir proveedor en la bodega
                    if opcion2 == 1:
                        limpiar()
                        print(f">>> Inscribir proveedor en {administradores[n].bodega.nombre} <<<\n")
                        for i in proveedores:
                            if administradores[n].bodega.proveedores.get(i) != None:
                                pass
                            else: print(proveedores[i])
                        p = int(input("\nSeleccione proveedor a inscribir: "))
                        administradores[n].bodega.proveedores[p] = proveedores[p]
                        input()
                        
                    # 2.2. Modificar tipo producto del proveedor.
                    elif opcion2 == 2:
                        limpiar()
                        print(f">>> Modificar tipo de producto de proveedor en {administradores[n].bodega.nombre}.\n")
                        for i in administradores[n].bodega.proveedores:
                            print(administradores[n].bodega.proveedores[i])
                        p = int(input("\nSeleccione proveedor: "))
                        t = input(f"Ingrese el nuevo tipo de producto del proveedor {administradores[n].bodega.proveedores[p].nombre}:  ").title()
                        administradores[n].bodega.proveedores[p].tipo_producto = t
                        
                        input()

                    # Volver
                    elif opcion2 == 3:
                        break
                    
                # Volver   
                elif opcion == 3:
                    break            
            
    # Acceso operario
    if opcion0 == 2:

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
                print("[1] Ver de proveedores por bodegas.")
                print("[2] Salir")
                
                opcion = int(input("\nSeleccione opción: "))
                
                if opcion == 1:
                    limpiar()
                    print(">>> Información de Bodegas <<\n")
                    for i in bodegas:
                        print("="*80)
                        print(f"{bodegas[i].nombre}\n")
                        print("\tProveedores:")
                        for j in bodegas[i].proveedores:
                            print(f"\t\t► {bodegas[i].proveedores[j].nombre}")
                    input() 
                    
                elif opcion == 2:
                    break 
    if opcion0 == 3:
        break
        
print("\nAdios!.")