# iterador= 0
# while iterador<5:
#     print("El iterador es: ", iterador)
#     iterador+=1

# contraseña_correcta="python123"
# contraseña_usuario=""
# while contraseña_usuario != contraseña_correcta:
#     contraseña_usuario=input("Ingrese su contraseña: ")
#     if contraseña_usuario!=contraseña_correcta:
#         print("contraseña incorrecta")
# else:
#         print("contraseña correcta")

# print("Bienvenido al programa")

# frutas=["manzana","pera","banano"]
# for fruta in  frutas :
#     print(fruta)
# mensaje="Hola  mundo"
# for caracter in mensaje:
#     print(caracter)

# numeros=[10,1,6,8,9]
# umbral=10
# for numero in numeros:
#     if numero>10:
#         print(f"El primer numero mayor que {umbral} es {numero}")
#         break
# else:
#     print(f"Ningun numero de la lista es mayor que {umbral}")

# while True:
#     texto=input("escribe algo(o 'salir'para terminar):")
#     if texto=="salir":
#         print("Adios")
#         break
# print(f"Escribiste:{texto}")

#Definicion de variables
# valor1=50

# def valorext():
#     resultadofinal=20
#     print(resultadofinal)
# valorext()
# print(valor1)

#ejercicio con array
# nums=[23,22,10,100]
# animals=["cat","dog","horse","snake"]
# def ShowFirstAndSecond(cosas):
#     first=cosas[0]
#     last=cosas[3]
#     return first,last

# animal1,animal2= ShowFirstAndSecond(animals)
# numero1,numero2=ShowFirstAndSecond(nums)

# print(animal1,animal2)
# print(numero1,numero2)

#funciones blandas: simplifica las funciones, se pueden hacer de forma resumida
# doblar=lambda x: x*2 
# resultado=doblar(40)
# print("el resultado es: ",resultado)

#ejemplo con lambda(funcion blanda)
# cotizaciones= lambda presupuesto,mano_de_obra: presupuesto+mano_de_obra
# resultado= cotizaciones(1000,2000)
# print("El resultado de la cotizacion es: ",resultado)

#agregar un numero al final
# lista=[5,10,15,20,25,50,100]
# lista.append(300)
# print(lista)
#agregar un numero en una posicion especifica
# lista=[5,10,15,20,25,50,100]
# lista.insert(2,300) #inserta el numero 300 en la posicion 2 
# print(lista)

#agregar varios 
# lista=[5,10,15,20,25,50,100]
# lista2=[5,11,15,50,25,200,100]
# lista.extend(lista2)#se agrega lista 2 porque es la que quiero fusionar con lista 1
# print(lista)

#remover la primera coincidencia
# lista=[5,11,15,50,25,5,200,100]
# lista.remove(5)##elimina la primera coincidencia ingresada
# print(lista)

#remover un dato en posicion especifica
# lista=[5,11,15,50,25,5,200,100]
# lista.pop(5)
# print(lista)

#vaciar la lista completa
# lista=[5,11,15,50,25,5,200,100]
# lista.clear()
# print(lista)

#contar cuantas veces esta un elemento en la lista
# lista=[5,11,15,50,25,5,200,100]
# apariciones=lista.count(5)
# print(f"el numero ingresado esta {apariciones}, veces")

# coders=[]
# print(coders)

# amount= int(input("Ingrese la cantidad de usuarios que desea agregar: "))

# while amount != 0:
#     name=input("Ingrese su nombre: ")
#     lastName=input("Ingrese su apellido: ")
#     age=int(input("Ingrese su edad: "))
#     email=input("Ingrese su correo: ")

#     coder={
#         "nombre":name,
#         "apellido":lastName,
#         "edad": age,
#         "correo":email
#         }
    
#     coders.append(coder)
#     amount-=1
#     print(f"Ha ingresado un usuario, le resta ingresar: {amount} usuario(s)")

# print(coders)

#solicitar año de nacimiento y verificar que sea numero
#solicitar dia de naciminieto y ciudad de nacimiento

# ciudad_de_nacimiento=input("Ingrese su ciudad de nacimiento: ")
# while True:
#     try:
#         año=int(input("Ingrese su año de nacimiento: "))
#         resta=2025-año
#         while resta <1 or resta >=100:
#             print("ingresaste un año que no concuerda con una edad real")
#             año=int(input("Ingrese su año de nacimiento: "))
#             resta=2025-año
    
#         while True:
#             try:
#                 dia=int(input("Ingrese su dia de nacimiento: ")) 
#                 while dia > 31:
#                     print("Un mes no tiene tantos dias..")
#                     dia=int(input("Ingrese su dia de nacimiento: "))                   
#                 break
#             except ValueError:
#                 print("Ingresaste un dia incorrecto: ")
#         break        
#     except ValueError:
#         print("Ingresaste un año incorrecto: ")




# creando funciones ejemplos:
def saludar():
    print("Buenos dias...")

saludar()

#$i quiero variar el saludo agregando el nombre
def saludar(nombre):
    print(f"Hola {nombre}, buenos dias...")
saludar("Marco")

#si quiero modificar la funcion con variables
# def saludo(nombre,sexo):
#     if sexo=="mujer":
#         adjetivo="señorita"
#     elif sexo=="hombre":
#         adjetivo="caballero"
#     else:
#         adjetivo="participante"

#     print(f"Hola {adjetivo} {nombre}, bienvenido al programa... ")

# saludo("mar","homr")

# numeros=[0]
# suma=bool(numeros)
# print(suma)



