import math
from math import sqrt
import math as m
import random
import datetime

# try:
#     numero = int(input("Introduce un número entero: "))
#     print("El doble es:", numero * 2)
# except:
#     print("Error: debes ingresar un número válido.")
# finally:
#     print("Fin del programa.")

print("Raíz:", math.sqrt(16))
print("Aleatorio:", random.randint(1, 10))
print("Fecha:", datetime.date.today())

import math
from datetime import date

def doble(n): return n * 2
def es_par(n): return n % 2 == 0
def area_circulo(r): return math.pi * r ** 2
def hoy(): return date.today().isoformat()

def convc_f(x):

    resultado=(x * (9/5)) + 32

    return print(resultado)

