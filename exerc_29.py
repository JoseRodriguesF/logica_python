#Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = ['','Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabádo']

dia = int(input("Digite um dia da semana em numero: "))
if 7 < dia <= 0:
    print("Dia inválido")
else:
    dia_semana = semana[dia]
    print(f"DIA: {dia_semana}")