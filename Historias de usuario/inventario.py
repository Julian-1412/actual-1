#  Entrada de datos (variables en Python):

#     Crea un archivo inventario.py.
#     Declara variables para nombre (string), precio (float) y cantidad (int).
#     Solicita al usuario estos datos con la función input().
#     Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
#     Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.

nombre=input("Ingrese el nombre del producto: ") 
while  True: #with this cicle I'm looking for the user to put what I'm asking him 
  
    try:    #] It verify that all data is correct
        precio=float(input("Ingrese el precio: ")) #float value
        while True: #with this cicle I'm looking for the user to put what I'm asking him 
            try: #verify that the data entered is an integer
                cantidad=int(input("Ingrese la cantidad: "))
                break #end the cycle if it is completed 
            except ValueError: #Catch the error in the quantity data to display the following message 
                print("Los datos son incorrectos")      
        break #Finish the cicle if it is completed
    except ValueError: #Catch the error in the price data to display the following message 
        print("Los datos son incorrectos")

# Operación matemática (costo total):

#     Crea una variable llamada costo_total.
#     Almacena en ella el resultado de multiplicar el precio por la cantidad (precio * cantidad).
#     Asegúrate de que la operación se realice después de validar los datos de entrada.

costo_total= precio*cantidad #The variable containing the operation that captures the data requested from the user is created.
print(f"El costo total es: {costo_total}")#print the opertion and show the result


# Mostrar resultados en consola:

#     Usa la función print() para mostrar un mensaje con:
#         Nombre del producto
#         Precio unitario
#         Cantidad
#         Costo total calculado
#     El formato del mensaje debe ser claro, por ejemplo: "Producto: Lápiz | Precio: 500 | Cantidad: 3 | Total: 1500"

print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}") # final result









        

