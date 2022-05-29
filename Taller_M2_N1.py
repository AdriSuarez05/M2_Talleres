# -*- coding: utf-8 -*-
"""
Created on Sat May 28 13:23:27 2022

@author: Adriana Suarez
"""

"""
email: adriana.suarezb@upb.edu.co
ID: 502197

"""

a = 2
b = 3
c = 5
d = 2
e = 7
f = 1


# Primer punto
ecu1 = (a + (b/c))/(d+(e/f))
print("El valor de la ecuación uno es: " )
print(ecu1)

# Segundo punto
ecu2 = a - (b/(c-d))
print("El valor de la ecuación dos es: " )
print(ecu2)
print("\n")

# Una vez terminado el punto 1 y 2 debe pasar el valor de "ecu1"
# a la variable "Ecu2" y el valorde la variable "Ecu2" a la variable "ecu1" 

print("Ecu1: ", ecu1, "Ecu2: ", ecu2, "\n")
temp = ecu1
ecu1 = ecu2
ecu2 = temp
print("Valores intercambiados")
print("Ecu1: ", ecu1, "Ecu2: ", ecu2)


