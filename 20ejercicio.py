#Agregar y eliminar frutas.
frutas=["manzana","pera","kiwi","mango","sandia","papaya","melon"]
#agregamos elemento a la lista
frutas.append("piña")
print(frutas)
#agregamois elemento en posicion especifica
frutas.insert(3,"fresa")
print(frutas)
#eliminamos un elemento en posicion especifica
frutas.pop(4)
print(frutas)
#eliminamos un elemento por nombre
frutas.remove("melon")
print(frutas)