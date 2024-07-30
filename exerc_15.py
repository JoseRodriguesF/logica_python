#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

valor_hora = float(input("Qual seu valor por hora trabalhada?: "))
horas_trabalhadas = int(input("Quantas horas você trabalha por mês?: "))

salario = valor_hora * horas_trabalhadas
imposto_de_renda = (11 / 100) * salario
inss = (8 / 100) * salario
sindicato = (5 / 100) * salario
salario_bruto = salario -(imposto_de_renda+inss+sindicato)


print(f"Salário: R${salario:.2f}\nIR: R${imposto_de_renda:.2f}\nINSS: R${inss:.2f}\nSindicato: R${sindicato:.2f}\nSalário bruto: R${salario_bruto:.2f}")





