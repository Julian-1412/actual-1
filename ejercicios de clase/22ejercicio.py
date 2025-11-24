datos=int(input("cuantos numeros desea ingresar: "))
lista=[]
print(f"Usted desea ingresar {datos} datos")
for i in range(datos):
    num1=float(input(f"ingrese la calificacion {i+1}: "))#se agrega i+1 porque en ciclos for empieza a contar desde 0 entonces mostraria al usuario: ingrese el dato cero, luego el dato uno y asi hasta ingresar la cantidad de datos que desea, por esta razon para que sea mas natura se agrega esa formula para que empiece desde uno
    lista.append(num1)
    print(lista)

promedio=sum(lista) / len(lista)#len=cuenta la cantidad de elementos de la lista, sum=suma los datos que hay en la lista
print(f"El promedio de la lista es: {promedio: .2f}")
#si quiero que el resultado salga con un numero determinado de decimales debo: colocar promedio: .2f