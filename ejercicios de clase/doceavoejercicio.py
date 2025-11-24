# dato1=int(input("Ingrese el primer valor: "))
# dato2=int(input("Ingrese el segundo valor: "))
# dato3=int(input("Ingrese el tercer valor: "))
# if dato1<dato3 and dato2<dato3:
#     print(f"el tercer numero ingresado {dato3}, es el mayor")
# elif dato1<dato2:
#     print(f"El segundo dato ingresado {dato2}, es el mayor")
# else:
#     print(f"El primer dato ingresado {dato1}, es el mayor")

dato1=int(input("Ingrese el primer valor: "))
dato2=int(input("Ingrese el segundo valor: "))
dato3=int(input("Ingrese el tercer valor: "))
mayor=max(dato1,dato2,dato3)
print(f"El dato mayor es: {mayor}")
menor=min(dato1,dato2,dato3)
print(f"El dato menor es: {menor}")