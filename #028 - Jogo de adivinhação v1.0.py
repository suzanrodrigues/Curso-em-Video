'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se  usuário venceu ou perdeu'''

import random, time                                            #Poderia usar o random.randint ou from random import randint
numero = [0, 1, 2, 3, 4, 5]
computador = random.choice(numero)                             #Faz o computador "PENSAR"
cores = {'limpa': '\033[m', 'amarelo': '\033[33m', 'verde': '\033[32m', 'vermelho': '\033[31m', 'negrito': '\033[1m'}
print('-=-' * 19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Escolha um número entre 0 a 5: '))        #Jogador tenta adivinhar
print('{}PROCESSANDO...{}'.format(cores['negrito'], cores['limpa']))
time.sleep(2)
if jogador == computador:
    print('{}\033[1mPARABÉNS! Você conseguiu me vencer!{}'.format(cores['verde'], cores['limpa']))
else:
    print('{}\033[1mGANHEI! Eu pensei no número {} e não no {}{}'.format(cores['vermelho'], computador, jogador, cores['limpa']))





