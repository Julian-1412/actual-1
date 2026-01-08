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
numero=int(input("Ingrese el numero que desea multiplicar: "))
print(f"A continuacion la tabla del {numero}")
for i in range(1,11):
    resultado= numero*i
    print(f"el resultado de la tabla es  {numero}*{i} = {resultado}")

# 6️⃣ Contar números positivos

# Pide números al usuario hasta que ingrese un 0.
# Muestra cuántos fueron positivos.

# 7️⃣ Nota final

# Pide una nota de 0 a 5 y muestra:

# ❌ Reprobó (menos de 3)

# ⚠️ Aprobó (3 a 4)

# ⭐ Excelente (más de 4)

# 8️⃣ Suma de los primeros N números

# Pide un número N y suma desde 1 hasta N.

# 🟠 Nivel 3 – Arreglos y lógica intermedia
# 9️⃣ Promedio de un arreglo

# Dado un arreglo de números, calcula el promedio.

# Ejemplo:

# [4, 5, 3, 2, 5]

# 🔟 Número mayor en un arreglo

# Encuentra el número más grande de una lista.

# 1️⃣1️⃣ Invertir un texto

# Pide una palabra y muéstrala al revés.

# Ejemplo:

# hola → aloh

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