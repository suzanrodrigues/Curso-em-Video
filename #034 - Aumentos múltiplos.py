'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a RS1500,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%'''

salario = int(input('Qual o salário do funcionário? R$'))

if salario <= 1500:
    print('O aumento do seu salario é de 15%, então seu salário será R${:.2f}'.format(salario * 0.15 + salario))
else:
    print('O seu aumento é de 10%, logo seu salário será R${:.2f}'.format(salario * 0.10 + salario))



