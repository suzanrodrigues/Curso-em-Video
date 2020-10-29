'''Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome'''

nome = input('Digite seu nome completo: ').strip()
if 'SILVA' in nome.upper():
    print('O seu nome tem Silva')
else:
    print('O seu nome não contém Silva')