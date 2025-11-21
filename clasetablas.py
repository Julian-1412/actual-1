#ejercicio tablas de multiplicar

# while True:
#     try:
#         dato=int(input("Ingrese un numero:")) 
#         with open(f"ejerciciotablas/tabla_{dato}.txt","w") as archivo:
#             for i in range(1,11):
#                 archivo.write(f"{dato} X {i}= {dato*i} \n")
#         break
#     except: 
#         print("Ingresaste un dato invalido, solo deben ser numeros")           

# with open("ejerciciotablas/tabla_5.txt","r") as line:
#     for linea in line:
#         print(linea)

#ejercicios de github

#ejericicio #1
# Ejercicio 1: Guardar frutas
# Solicita al usuario 5 frutas y guárdalas en frutas.txt, una por línea.

# with open("prueba-b/ejerciciotablas/frutas.txt","w") as frutas:
#     for fruta in range(5):
#         nombre= input("Ingrese el nombre de una fruta: ")
#         frutas.write(f"{fruta+1} {nombre} \n")

#ejercicio #2
# Ejercicio 2: Contar líneas
# Lee un archivo de texto y muestra cuántas líneas contiene.  
# opcion 1 
# with open("prueba-b/ejerciciotablas/frutas.txt","r") as lectura:
#    contenido=lectura.readlines()
#    print(f"El archivo contiene  {len(contenido)} lineas") 
#opcion 2

# contador=0
# with open("prueba-b/ejerciciotablas/frutas.txt","r") as lineas:
#     for linea in lineas:
#         contador += 1
#     print(f"El archivo tiene {contador} lineas")

#Ejercicio 3: Buscar una palabra
#Pide una palabra y muestra todas las líneas de un archivo donde aparezca.

with open("prueba-b/ejerciciotablas/frutas.txt","r") as busqueda:
    fruta=input("Ingrese la fruta que desea buscar: ")
    for linea in busqueda:
        if fruta in linea:
            print(f"La fruta ingresada {fruta} esta en la linea numero:  {linea}")



