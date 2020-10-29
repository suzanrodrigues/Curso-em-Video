'''Desenvolva um programa que pergutne a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas'''

distancia = int(input('Quantos é a distância da sua viagem? '))
#preço = distancia * 0.50 if distancia <=200 else distancia * 0.45  ----> IF simplificado
if distancia <= 200:
    print('O valor da sua passagem é de R${:.2f}'.format(distancia * 0.50))
else:
    print('O valor da sua passagem é de R${:.2f}'.format(distancia * 0.45))

