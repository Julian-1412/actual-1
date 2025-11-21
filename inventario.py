#  Entrada de datos (variables en Python):

#     Crea un archivo inventario.py.
#     Declara variables para nombre (string), precio (float) y cantidad (int).
#     Solicita al usuario estos datos con la función input().
#     Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
#     Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.

nombre=input("Ingrese el nombre del producto: ") #variable que solicita al usuario el ingreso de el dato
while  True: #ciclo que busca el cumplimiento de ciertas condiciones
  
    try:    # verifica que los datos ingresados sean permitidos    
        precio=float(input("Ingrese el precio: ")) #variable que busca el ingreso de un dato flotante
        while True: #ciclo que busca que el dato ingresado cumpla con lo esperado 
            try: #verifica que el dato ingresado sea un numero entero
                cantidad=int(input("Ingrese la cantidad: "))
                break #finaliza el ciclo si se cumplio 
            except ValueError: #atrapa el error en el dato de cantidad para arrojar el siguiente mensaje 
                print("Los datos son incorrectos")      
        break #finaliza el ciclo si se cumplio
    except ValueError: #atrapa el error en el dato de precio para arrojar el siguiente mensaje 
        print("Los datos son incorrectos")

# Operación matemática (costo total):

#     Crea una variable llamada costo_total.
#     Almacena en ella el resultado de multiplicar el precio por la cantidad (precio * cantidad).
#     Asegúrate de que la operación se realice después de validar los datos de entrada.

costo_total= precio*cantidad #se crea la variable que contiene la operacion que atrapa los datos solicitados al usuario
print(f"El costo total es: {costo_total}")#imprime la operacion y entrega el resultado en consola


# Mostrar resultados en consola:

#     Usa la función print() para mostrar un mensaje con:
#         Nombre del producto
#         Precio unitario
#         Cantidad
#         Costo total calculado
#     El formato del mensaje debe ser claro, por ejemplo: "Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500"

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}") # resultado final que entrega en consola los datos ingresados por el usuario y su operacion









        

