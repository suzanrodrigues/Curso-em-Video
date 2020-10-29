'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"'''

cidade = input('Digite o nome da sua cidade: ').strip()
cap = cidade.capitalize()
if 'Santo' in cap:
    print('A sua cidade começa com a palavra Santo!')
else:
    print('A sua cidade não começa com a palavra Santo!')