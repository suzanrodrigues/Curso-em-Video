"""Crie um programa que leia um número Real qualquer pelo teclado e moste na tela a sua porção inteira"""

from math import floor
num = float(input('Digite um número: '))
int = floor(num)
print('O número {} tem a parte inteira {}'.format(num, int))

'''outro exemplo:
from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua parte inteira é {}'.format(num, trunc(num)))

ou ainda mais simples

num = float(input('Digite um valor: '))
print(O valor digitado foi {} e a sua parte inteira é {}'.format(num, int(num)))
'''