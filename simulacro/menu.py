# 1. Gestión del inventario

#     Registrar, consultar, actualizar y eliminar productos.\
#     Cada producto debe incluir:
#         Nombre del producto\
#         Marca\
#         Categoría\
#         Precio unitario\
#         Cantidad en stock\
#         Garantía en meses

    # print("1. Nombre del producto")
    # print("2. Marca")
    # print("3. Categoría")
    # print("4. Precio unitario")
    # print("5. Cantidad en stock")
    # print("6. Garantia en meses")
    # print("7. Salir")



from utils import saludar_usuario

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Registrar")
    print("2. Consultar")
    print("3. Actualizar")
    print("4. Eliminar ṕroducto")  
    print("5. Salir")
    
    
    try:    
        opcion = int(input("\nSelecciona una opción (1-7): "))
        if opcion == 1:
            print("✓ Opción 1 seleccionada")
            while True:
                print("1. Registar Producto")
                print("2. Registar Cliente")
                print("3. Salir")
                opcion = int(input("\nSelecciona una opción (1-2): "))
                if opcion == 1:
                    nombre_producto=input("Ingrese el nombre del producto: ")                  
                    marca=input("Ingrese la marca: ")
                    categoria=input("Ingrese la categoria del producto: ")
                    precio_unitario=float(input("Ingrese el precio del producto: "))
                    stock=int(input("Ingrese la cantidad disponible: "))
                    garantia=int(input("Ingrese el tiempo de garantia en meses: "))
                elif opcion == 2: 
                    cliente=input("Ingrese el nombre del cliente: ")                  
                    tipo_cliente=input("Ingrese el tipo de cliente: ")
                    producto_vendido=input("Ingrese el nombre del producto: ")
                    cantidad_producto=int(input("Ingrese la cantidad del producto: "))
                    fecha_venta=input("Ingrese la fecha de venta: ")
                    descuento_aplicado=float(input("Ingrese el descuento dado: "))    
                elif opcion == 3:
                    print("Escogio la opcion salir")
                    break
                else:
                    print("Esta opcion no es valida...")             


        elif opcion == 2:
            print("✓ Opción 2 seleccionada")
        elif opcion == 3:
            print("✓ Opción 3 seleccionada")
        elif opcion == 4:
            print("✓ Opción 4 seleccionada")
        elif opcion == 5:
            print("✓ Opción 5 seleccionada")
        elif opcion == 6:
            print("✓ Opción 6 seleccionada")
        elif opcion == 7:
            print("✓ Saliendo del programa...")
            break
        else:
            print("✗ Opción no válida")
    except:
        print("Ingresaste una opcion invalida...")