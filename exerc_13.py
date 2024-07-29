#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
escolha = int(input("1-Homem\n2-Mulher\nDigite: "))

if escolha == 1:
    print("Homem")
    h = float(input("Digite sua altura: "))

    peso = (72.7*h) - 58

    print("Seu peso ideal é: ", round(peso, 2))

elif escolha == 2:
    print("Mulher")
    h = float(input("Digite sua altura: "))

    peso = (62.1*h) - 44.7

    print("Seu peso feminino ideal é: ", round(peso, 2))

else:
    print("Digite uma opção válida")
