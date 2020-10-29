'''Faça um programa que leia uma frase pelo teclado e mostra:
Quantas vezes aparece a letra A
Em que posição ela aparece pela primeira vez
Em que posição ela aparece a última vez'''

a = str(input('Digite uma frase: ')).upper().strip()
print('A letra "A" aparece {} vezes'.format(a.count('A')))
print('A letra "A" aparece na posição {}'.format(a.find('A')+1))
print('Ela aparece pela última vez na posição {}'.format(a.rfind('A')+1))
