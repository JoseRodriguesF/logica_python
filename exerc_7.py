#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input("Digite o seu salario por hora: "))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas por mes: "))

salario = valor_hora*horas_trabalhadas

print("seu salario é: ", salario)