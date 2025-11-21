num1=int(input("ingrese el primer numero: "))
num2=int(input("Ingrese el segundo numero: "))
pregunta=input("Que tipo de operacion desea realizar?: +,-,*,/ : ")
if pregunta=="+":
    print("El resultado de la suma es:",num1+num2)
elif pregunta=="-":
    print("El resultado de la resta es:",num1-num2)
elif pregunta=="*":
    print("El resultado de la multiplicacion es:",num1*num2)
elif pregunta=="/":
      print("El resultado de la division es:",num1/num2)

else:
    print("Ingreso un caracter invalido")