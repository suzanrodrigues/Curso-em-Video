"""Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 o dia e R$0,15 por Km rodado."""

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
calckm = km * 0.15
calcdias = dias * 60
print('O total a pagar é de R${:.2f}'.format((km * 0.15) + (dias * 60)))

