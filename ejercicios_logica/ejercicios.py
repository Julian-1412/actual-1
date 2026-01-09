# 1️⃣ Suma de dos números

# Pide dos números al usuario y muestra la suma.

# Pista: variables + entrada + salida.

# num1= int(input("ingrese un numero: "))
# num2= int(input("Ingrese el segundo numero: "))
# suma= num1+num2
# print(f"El resultado de la suma es: {suma}")

# 2️⃣ Número par o impar

# Pide un número e indica si es par o impar.

# Pista: operador módulo %.

# numero=int(input("Ingresese un numero para determinar si es par o impar: "))
# if numero %2==0:
#     print(f"El numero que ingresaste '{numero}' es par")
# else:
#     print(f"El numero que ingresaste '{numero}' es impar")

# 3️⃣ Mayor de dos números

# Pide dos números y muestra cuál es el mayor o si son iguales.
# num1=int(input("Ingrese el primer numero: "))
# num2=int(input("Ingrese el segundo numero: "))
# if num1<num2:
#     print("El segundo numero es mayor que el primero")
# elif num1>num2:
#     print("El primer numero es mayor que el segundo")
# else:
#     print("Los numeros son iguales")

# 4️⃣ Conversión de temperatura

# Convierte grados Celsius a Fahrenheit.

# Fórmula:

# F = (C × 9/5) + 32
# try:
#     celsius=float(input("Ingrese la temperatura en grados Celsius: "))
#     conversion= ((celsius*(9/5)+32))
#     print(f"La temperatura ingresada en grados Celsius '{celsius}' pasa a grados Farenheit en: {conversion}")
# except ValueError:
#     print("Ingresa un valor numerico")    

# 🟡 Nivel 2 – Condicionales y ciclos
# 5️⃣ Tabla de multiplicar

# Pide un número y muestra su tabla del 1 al 10.
# numero=int(input("Ingrese el numero que desea multiplicar: "))
# print(f"A continuacion la tabla del {numero}")
# for i in range(1,11):
#     resultado= numero*i
#     print(f"el resultado de la tabla es  {numero}*{i} = {resultado}")

# 6️⃣ Contar números positivos

# Pide números al usuario hasta que ingrese un 0.
# Muestra cuántos fueron positivos.


# contador_numeros_positivos=0
# while True:
#     try:
#         num= int(input("Ingresa un numero:"))
#         if num >0:
#             print("El numero que ingresaste es positivo")
#             contador_numeros_positivos+=1
#             print(f"Llevas ingresados {contador_numeros_positivos} numeros positivos")
#         elif num==0:
#             print("Ingresaste el numero 0, gracias por participar")
#             break
#         else:
#             print("Ingresaste un numero negativo")
#     except ValueError:
#         print("Ingresa un numero entero")
# 7️⃣ Nota final

# Pide una nota de 0 a 5 y muestra:

# ❌ Reprobó (menos de 3)

# ⚠️ Aprobó (3 a 4)

# ⭐ Excelente (más de 4)
# try:
#     nota= float(input("Ingresa la nota del estudiante: "))
#     if nota >4 and nota <=5:
#             print("La nota es excelente!")
#     elif nota >=3 and nota <=4:
#          print("El estudiante aprobo :) ")
#     elif nota >=0 and nota <3:
#          print("La nota es inferior a 3 por lo tanto reprobo :(")
# except ValueError:
#         print("Ingresa un numero valido")


# 8️⃣ Suma de los primeros N números

# Pide un número N y suma desde 1 hasta N.


# try:
#     numero=int(input("Ingresa un numero: "))
#     if numero<1:
#         print("Ingresa un numero valido")
#     else:
#         suma=0
#         for num in range(1, numero+1):
#             suma+=num
#         print(f"La suma de los numero del 1 al {numero} es: {suma} ")
# except ValueError:
#     print("Ingresa un numero entero")




# 🟠 Nivel 3 – Arreglos y lógica intermedia
# 9️⃣ Promedio de un arreglo

# Dado un arreglo de números, calcula el promedio.

# Ejemplo:

# [4, 5, 3, 2, 5]
#opcion numero uno utilizando for
#notas=[4,5,3,2,4,5,5]
# contador=0
# for nota in notas:
#     contador+=nota
# promedio= contador/len(notas)
# print(f"El promedio de notas de la lista es: {promedio:.2f}")
#opcion numero dos mas simple 
# notas=[4,5,3,2,4,5,5]
# promedio= sum(notas)/len(notas)
# print(f"El promedio de las notas de la lista es: {promedio:.2f}")



# 🔟 Número mayor en un arreglo

# Encuentra el número más grande de una lista.
 #opcion 1 mas sencilla
# lista=[200,22,60,78,961,521,1020,951]
# print(max(lista))
#opcion dos con ciclo for
# lista=[200,22,60,78,961,521,12500,1020,951,5001]
# mayor=lista[0] #se define esta variable para que el valor inicial siempre sea el mas alto, sin importar si en la lista se encuentra el valor cero o numeros negativos,
#                 #sucederia un error si le digo a la variable que inicie desde cero, asi no podria evaluar una lista con valores negativos
# for list in lista:
#     if list > mayor:
#         mayor=list
# print(f"El numero mayor de la lista es: {mayor}") 


# 1️⃣1️⃣ Invertir un texto

# Pide una palabra y muéstrala al revés.

# Ejemplo:

# hola → aloh
#opcion 1 
# palabra=input("Ingresa una palabra: ")
# invertida=""
# for i in palabra:
#     invertida= i+invertida
# print(f"La palabra que ingresaste '{palabra}' invertida es: {invertida}")
#opcion 2 utilizando for range:
# palabra=input("Ingresa una palabra: ")
# invertida=""
# for i in range( len(palabra)-1,-1, -1):
#     invertida+= palabra[i]
# print(invertida)
#opcion 3 con slice
palabra=input("Ingresa una palabra: ")
palabra_invertida=palabra[::-1]
print(palabra_invertida)

# 1️⃣2️⃣ Contar vocales

# Cuenta cuántas vocales tiene una palabra.

# 🔴 Nivel 4 – Retos lógicos
# 1️⃣3️⃣ FizzBuzz

# Del 1 al 100:

# Múltiplo de 3 → Fizz

# Múltiplo de 5 → Buzz

# Ambos → FizzBuzz

# 1️⃣4️⃣ Número primo

# Pide un número y determina si es primo.

# 1️⃣5️⃣ Cajero automático

# Simula un cajero:

# Saldo inicial

# Retiro

# Validar si hay fondos suficientes