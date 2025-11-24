#Buscar un elemento en la lista.
frutas=["manzana","pera","kiwi","mango","sandia","papaya","melon"]
usuario=input("Escriba el nombre de la fruta que desea encontrar en la lista: ")
# if usuario in frutas:
#     print(f"{usuario} esta dentro de la lista, {frutas}")
# else:
#     print("La fruta no esta en la lista")
for i,fruta in enumerate(frutas):
    if usuario==fruta:

        print(f"La fruta: {fruta} esta en la posicion {i}")
else:
    print("La fruta ingresada no esta en la lista")