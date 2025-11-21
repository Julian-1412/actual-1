import random 
numero_random= random.randint(1,15)
intento=int(input("Ingrese un numero entre(1-15): "))

while intento!=numero_random:
    if intento<numero_random:
        print("El numero ingresado es menor")
    else:
        print("El numero ingresado es mayor")
    #intento=int(input("Ingrese un numero entre(1-15): "))
print("Lo lograste!!!")

