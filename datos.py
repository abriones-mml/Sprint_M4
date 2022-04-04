from clase_usuario import Usuario
from clase_operario import Operario
from clase_administrador import Administrador
from clase_bodega import Bodega
from clase_proveedor import Proveedor
from clase_producto import Producto

# Proveedores
tipo_producto = {1: "Tecnología", 2: "Calzado", 3: "Casa y Decoración", 4: "Deportes", 5: "Vestuario"}
pv1 = Proveedor(1, "Proveedor 1", tipo_producto[1])
pv2 = Proveedor(2, "Proveedor 2", tipo_producto[2])
pv3 = Proveedor(3, "Proveedor 3", tipo_producto[3])
pv4 = Proveedor(4, "Proveedor 4", tipo_producto[4])
pv5 = Proveedor(5, "Proveedor 5", tipo_producto[5])
proveedores = {1: pv1, 2: pv2, 3: pv3, 4: pv4, 5: pv5}

# Productos
a1 = Producto("Smartphone X67", pv1, 139000)
a2 = Producto("Zapatillas Vands", pv2, 49000)
a3 = Producto("Sofa Cama", pv3, 60000)
a4 = Producto("Camiseta Shile rumbo a Qatar 2022", pv4, 9990)
a5 = Producto("Poleron Negro", pv5, 14990)
productos= {1: a1, 2: a2, 3: a3, 4: a4, 5: a5}



provb1 = {1:pv1, 2:pv2}
prodb1 = {1:a1, 2:a2}

proveedoresb1 = [provb1, prodb1] # lista (proveedores, productos)


provb2 = {3:pv3, 4:pv4}
prodb2 = {3:a3, 4:a4}

proveedoresb2 = [provb2, prodb2] # lista (proveedores, productos)

provb3 = {1:pv1, 3:pv3, 5:pv5}
prodb3 = {1:a1, 3:a3, 5:a5}

proveedoresb3 = [provb3, prodb3] # lista (proveedores, productos)

# Dict de stock de productos por bodega

a={1: 10, 2: 20}
b={3: 30, 4: 40} 
c={1: 50, 3: 60, 5: 70}

stockes = {1: a, 2: b, 3: c}

# Bodegas
b1 = Bodega(1, "Bodega 1", 1000, provb1, prodb1, a)
b2 = Bodega(2, "Bodega 2", 1000, provb2, prodb2, b)
b3 = Bodega(3, "Bodega 3", 1000, provb3, prodb3, c)
bodegas = {1: b1, 2: b2, 3: b3}

o1 = Operario(b1, "Elton", "Torron", 22022001, 2, 123)
o2 = Operario(b2, "Esteban", "Dido", 22022002, 2, 1234)
o3 = Operario(b2, "Giovanni", "Durán", 22022003, 2, 12345)
o4 = Operario(b3, "Toribio", "Jiménez", 22022004, 2, 123456)

a1 = Administrador(bodegas[1], "Giselle", "Saa", 12022001, 1, 1234)
a2 = Administrador(bodegas[2], "Elza", "Pallo", 12022002, 1, 12345)
a3 = Administrador(bodegas[3], "Ivette", "Farías", 12022002, 1, 123456)

administradores = {1: a1, 2: a2, 3: a3}
operarios = {1: o1, 2: o2, 3: o3, 4: o4}

# Transferencias
transb1 = []
transb2 = []        # [unidades, producto, destino]
transb3 = []

transfer = [transb1, transb2, transb3]