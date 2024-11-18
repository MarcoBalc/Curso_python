'''Escribe un programa que solicite al usuario un número entero y calcule
su cuadrado y su cubo.
--------------------------
numero =int(input("Ingresa un numero entero: "))
cuadrado= numero**2
cubo= numero**3
print(cuadrado)
print(cubo)
'''

import math

numero=int(input("ingresa un numero entero"))
cuadrado= math.pow(numero,2)
cubo= math.pow(numero,3)
print(cuadrado)
print(cubo)
