inventario=[] #data will be conatin in this list

def agregar_producto():
    nombre=input("Ingrese el nombre del producto: ")
    precio=float(input("Ingrese el precio del producto: "))
    cantidad=int(input("Ingrese la cantidad del producto: "))

    diccionario={
        "Nombre": nombre,
        "Precio": precio,
        "Cantidad": cantidad
    }
    inventario.append(diccionario) #with this method data will be added to the list
   
def mostrar_inventario(): #function that will show de dictionary
    if inventario==[]:
        print("El inventario esta vacio")
    else:    
        for mostrar in inventario: #with this cicle is posible to print de dictionary
            print(f"Nombre: {mostrar['Nombre']} | Precio: {mostrar['Precio']} | Cantidad: {mostrar['Cantidad']}")



def calculador_estadisticas(): # with this function is posible to do math operations
    if inventario == []:
        print("El inventario esta vacio")
        return

    costo_total=0
    cantidad_total=0

    for i in inventario: #with this cicle we can do math operations
        costo_total += i["Precio"]*i["Cantidad"]
        cantidad_total += i["Cantidad"]
    print(f"El valor total del inventario es: {costo_total}")
    print(f"La cantidad de productos que hay en el inventario es: {cantidad_total}")
    
    




while True: #this cicle will ask options to the user
    print("*"*5,"Bienvenido a su Menu","*"*5,"\n")
    try:     # with this we are gonna valid that data is correct
        saludo=(int(input(""" Por favor ingrese el numero de la opcion que desea utilizar: 
    (1) Agregar producto
    (2) Mostrar inventario
    (3) Calcular estadisticas
    (4) Salir
        """)))
        if saludo == 1:
            print("Elegiste la opcion agregar un producto")
            agregar_producto()
        elif saludo == 2:
            print("Elegiste la opcion mostrar inventario")
            mostrar_inventario()
        elif saludo == 3:
            print("Elegiste la opcion calcular estadistica")
            calculador_estadisticas()
        elif saludo == 4:
            print("Elegiste la opcion salir, hasta luego...")
            break
        else:
            print("Elegiste una opcion que no se encuentra en el menu, intentalo de nuevo")

    except: 
        print("Ingresaste un valor no permitido, intentalo de nuevo \n")





























