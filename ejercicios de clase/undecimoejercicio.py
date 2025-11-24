nota=float(input("Ingrese su nota: "))
if nota>=4.8 and nota<=5:
    print("Su nota es excelente!")
elif nota>=3 and nota<4.8:
    print("Su nota ha sido aprobada")
elif nota<3 and nota>=0:
    print("su nota ha sido reprobada")
else:
    print("Ingresaste un dato incorrecto")
