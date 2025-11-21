from utils import convc_f

# n = int(input("Número: "))
# print(utils.doble(n))
# print(utils.es_par(n))


# print(utils.convc_f(x))  otra opcion
while True:
    try:
        x=int(input("Ingrese el dato de temperatura en centigrados: "))
        convc_f(x)
        break     
    except:
        print("Ingresaste un dato invalido")

    finally:
        print("El programa termino")
