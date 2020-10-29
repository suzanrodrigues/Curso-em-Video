'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo (sem considerar espaços)
Quantas letras tem o primeiro nome'''

nome = str(input('Digite o seu nome: ')).strip() #strip para eliminar espaços antes e depois do nome caso o usuário insira
print(nome.upper())
print(nome.lower())
print('O seu nome completo tem {} letras'.format(len(nome) - nome.count(' ')))
name = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras!'.format(name[0], len(name[0])))

