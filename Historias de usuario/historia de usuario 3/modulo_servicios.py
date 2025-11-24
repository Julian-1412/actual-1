# agregar_producto(inventario, nombre, precio, cantidad)
# mostrar_inventario(inventario)
# buscar_producto(inventario, nombre) → retorna el dict o None
# actualizar_producto(inventario, nombre, nuevo_precio=None, nueva_cantidad=None)
# eliminar_producto(inventario, nombre)
# calcular_estadisticas(inventario) → retorna tupla/dict con métricas

def agregar_producto(inventario,nombre,precio,cantidad):
    "created to add prodcuts"
    inventario.append({
    "nombre":nombre,
    "precio":precio,
    "cantidad":cantidad
    })

def mostrar_inventario(inventario):
    """Muestra todos los productos del inventario"""
    if not inventario:
        print("\n✗ El inventario está vacío\n")
        return  
    print("\n--- INVENTARIO ACTUAL ---")
    for idx, producto in enumerate(inventario):
        print(f"{idx}. Nombre: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")
    print() 



def buscar_producto(inventario, nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None   

def actualizar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a actualizar: ")

    producto = buscar_producto(inventario, nombre)

    if not producto:
        print("✗ El producto no existe")
        return

    print(f"Producto actual: {producto}")

    nuevo_precio = input("Nuevo precio (Enter para no cambiar): ")
    nueva_cantidad = input("Nueva cantidad (Enter para no cambiar): ")

    if nuevo_precio:
        producto["precio"] = float(nuevo_precio)
    if nueva_cantidad:
        producto["cantidad"] = int(nueva_cantidad)

    print(" Producto actualizado correctamente")

def eliminar_producto(inventario):
    nombre = input("Ingrese el nombre del producto a eliminar: ")

    producto = buscar_producto(inventario, nombre)

    if not producto:
        print(" El producto no existe")
        return

    inventario.remove(producto)
    print(" Producto eliminado correctamente")

    
def estadisticas(inventario):
    """Muestra estadísticas generales del inventario"""

    if not inventario:
        print("\n✗ No hay estadísticas porque el inventario está vacío.\n")
        return
    
    total_productos = len(inventario)
    total_unidades = sum(p["cantidad"] for p in inventario)
    valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)

    # Producto con mayor stock
    mayor_stock = max(inventario, key=lambda p: p["cantidad"])

    # Producto más costoso
    mas_caro = max(inventario, key=lambda p: p["precio"])

    print("\n--- ESTADÍSTICAS DEL INVENTARIO ---")
    print(f"Total de productos diferentes: {total_productos}")
    print(f"Total de unidades en inventario: {total_unidades}")
    print(f"Valor total del inventario: ${valor_total:.2f}")
    print(f"Producto con mayor stock: {mayor_stock['nombre']} ({mayor_stock['cantidad']} unidades)")
    print(f"Producto más costoso: {mas_caro['nombre']} (${mas_caro['precio']})")
    print("----------------------------------------\n")