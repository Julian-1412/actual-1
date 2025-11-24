#Números pares: guardar solo los pares.

lista=[5,8,6,9,20,6,6,6,84,63,91,26]
lista_pares=[]
for i in lista:
    if i % 2==0:
        lista_pares.append(i)
print(f"los numeros pares de la lista son: {lista_pares}")        
 