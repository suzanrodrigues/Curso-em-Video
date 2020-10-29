'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados
 Ex.:
 Digite um númerero: 1834

 unidade: 4
 dezena: 3
 centena: 8
 milhar: 1'''

import math
numero = str(input('Digite um número na tela: '))
tamanho = len(numero)

if tamanho == 4:
    unidade = numero[3:4]
    dezena = numero[2:3]
    centena = numero[1:2]
    milhar = numero[0:1]
    print('A unidade do seu numero é {}, a dezena é {}, a centena é {} e o milhar é {}'.format(unidade, dezena, centena, milhar))

elif tamanho == 3:
    unidade = numero[2:3]
    dezena = numero[1:2]
    centena = numero[0:1]
    print('A unidade do seu numero é {}, a dezena é {}, a centena é {}'.format(unidade, dezena, centena))

elif tamanho == 2:
    unidade = numero[1:2]
    dezena = numero[0:1]
    print('A unidade do seu numero é {} e a dezena é {}'.format(unidade, dezena))

else:
    print('A unidade do seu numero é {}'.format(unidade))


