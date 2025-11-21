#Sumar hasta que el usuario escriba 0.
dato= int(input("Ingrese un numero: "))
suma_total=0
while dato!=0:
    suma_total=suma_total+dato
    print(f"Sigue intentando, la suma acumulada es: {suma_total}")
    dato=int(input("Ingrese un numero de nuevo: "))
print("Ingresaste el numero 0, gracias por participar")