from modulo_servicios import agregar_producto, mostrar_inventario, buscar_producto,actualizar_producto, eliminar_producto


while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Agregar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Actualizar")
    print("5. Eliminar")
    print("6. Estadisticas")
    print("7. salir")

    
    opcion = input("\nSelecciona una opción (1-7): ")
    
    if opcion == "1":
        print("✓ Opción 1 seleccionada")
        nombre=input("Ingrese el nombre del prodcuto: ")
        precio=float(input("Ingrese el precio del producto: "))
        cantidad=int(input("Ingrese la cantidad del producto: "))
        agregar_producto()        
    elif opcion == "2":
        print("✓ Opción 2 seleccionada")
        mostrar_inventario()
    elif opcion == "3":
        print("✓ Opción 3 seleccionada")
        buscar_producto()
    elif opcion == "4":
        print("✓ Opción 4 seleccionada")
        actualizar_producto()
    elif opcion == "5":
        print("✓ Opción 5 seleccionada")
        eliminar_producto()
    elif opcion == "6":
        print("✓ Opción 6 seleccionada")        
    elif opcion == "7":
        print("✓ Saliendo del programa...")
        break
    else:
        print("✗ Opción no válida")
