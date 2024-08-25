#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o novo salário, após o aumento.

Salario = float(input("Qual é seu salário?: "))

if Salario <= 280:
    Salario_reajuste = Salario + Salario * 0.2
    print(f"Salario reajustado: {Salario_reajuste}\nSalario anterior: {Salario}\nAumento: 20%\n")

elif 700 >= Salario >= 280:
    Salario_reajuste = Salario + Salario * 0.15
    print(f"Salario reajustado: {Salario_reajuste}\nSalario anterior: {Salario}\nAumento: 15%\n")

elif 700 <= Salario <= 1500:
    Salario_reajuste = Salario + Salario * 0.10
    print(f"Salario reajustado: {Salario_reajuste}\nSalario anterior: {Salario}\nAumento: 10%\n")

elif Salario > 1500:
    Salario_reajuste = Salario + Salario * 0.05
    print(f"Salario reajustado: {Salario_reajuste}\nSalario anterior: {Salario}\nAumento: 5%\n")




