'''Faça um programa que leia o nome completo de uma pessoa mostrando em seguida o primeiro e o último nome separadamente
Ex.: Ana Maria de Souza
primeiro = Ana
último: Souza'''

nome = input('Digite o nome de uma pessoa: ')
name = nome.split()
print('Primeiro: {}'.format(name[0]))
print('Último: {}'.format(name[-1]))

