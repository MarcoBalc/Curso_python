'''
Escribe un programa que solicite al usuario dos números y muestre su
suma, resta, multiplicación, división, división entera y residuo (módulo).

'''
num1=float(input("ingresar el primer número: "))
num2=float(input("ingresar el segundo número: "))
suma=num1+num2
resta=num1-num2
mult=num1*num2
division=num1/num2 if num2 !=0 else "no se puede dividir entre cero"
divisionEntera=num1//num2 if num2 !=0 else "no se puede dividir entre cero"
modulo=num1%num2 if num2 !=0 else "no se puede dividir entre cero"
print(f"suma:{suma}")
print(f"resta:{resta}")
print(f"multiplicacion:{mult}")
print(f"division:{division}")
print(f"divisionEntera:{divisionEntera}")
print(f"modulo:{modulo}")
