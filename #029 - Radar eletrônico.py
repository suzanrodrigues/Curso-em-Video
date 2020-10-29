'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite'''

vel = float(input('Qual a velocidade do carro: '))                          #Verifica a velocidade do motorista
if vel > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h.')
    a = (vel - 80) * 7                                                      #Calcula o calor da multa
    print('Você deverá pagar uma multa de RS{:.2f} reais!'.format(a))
print('Tenha um bom dia! Dirija sempre com segurança!')

