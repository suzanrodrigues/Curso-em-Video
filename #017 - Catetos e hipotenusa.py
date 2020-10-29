"""Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de uma triângulo retângulo,
calcule e mostre o comprimento da hipotenusa"""

from math import pow, sqrt
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = pow(co, 2) + pow(ca, 2) #vide exemplo abaixo nos comentários
print('O comprimento da hipotenusa é igual a {:.2f}'.format(sqrt(h)))

'''
## calculando matematicamente:
hipotenusa = (co ** 2 + ca ** 2) **(1/2)

##de maneira mais eficaz:
import math // from math import hipot
hipotenusa = math.hipot(co, ca)
'''




