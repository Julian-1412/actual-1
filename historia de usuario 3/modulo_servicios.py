# agregar_producto(inventario, nombre, precio, cantidad)
# mostrar_inventario(inventario)
# buscar_producto(inventario, nombre) → retorna el dict o None
# actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
# eliminar_producto(inventario, nombre)
# calcular_estadisticas(inventario) → retorna tupla/dict con métricas

def agregar_producto(inventario,nombre,precio,cantidad):
    """created to add prodcuts"""
    nombre=input("Ingrese el nombre del prodcuto: ")
    precio=float(input("Ingrese el precio del producto: "))
    cantidad=int(input("Ingrese la cantidad del producto: "))
    inventario.append({""
    "nombre":nombre,
    "precio":precio,
    "cantidad":cantidad
    })

def mostrar_inventario(inventario):
    """It will show all the productos or if there is not """
    if not inventario:
        print("El inventario esta vacio") 
        return
    for i in inventario:
        print(f"{i['nombre']}, {i['precio']}, {i['cantidad']} ")


def buscar_producto(inventario,nombre):
    """It will search an especific product"""
    for i in inventario:
        if i['nombre']==nombre:
            return i
    return None    #if the dictionary is empty

def actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    """It will add a new price or quantity if the product exist"""
    producto = buscar_producto(inventario, nombre)
    if producto:
        if nuevo_precio is not None:
            producto["precio"] = nuevo_precio
        if nueva_cantidad is not None:
            producto["cantidad"] = nueva_cantidad
        return True
    return False

def eliminar_producto(inventario, nombre):
    """It will delete a producto """
    producto = buscar_producto(inventario, nombre)
    if producto:
        inventario.remove(producto)
        return True
    return False

    
