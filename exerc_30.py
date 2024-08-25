# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
#   Média de Aproveitamento  Conceito
#   Entre 9.0 e 10.0        A
#   Entre 7.5 e 9.0         B
#   Entre 6.0 e 7.5         C
#   Entre 4.0 e 6.0         D
#   Entre 4.0 e zero        E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a sua nota: "))
nota2 = float(input("Digite a sua nota: "))

media = (nota1 + nota2)/2 
tabela = "Média de aproveiramento | Conceito\nEntre 9.0 e 10.0        | A\nEntre 7.5 e 9.0         | B\nEntre 6.0 e 7.5         | C\nEntre 4.0 e 6.0         | D\nEntre 4.0 e 0           | E"


if 9.0 <= media <= 10.0:
    conceito = "A"
    print(tabela, f"\n\nMedia: {media}\nResultado: {conceito}")

elif 7.5 <= media < 9.0:
    conceito = "B"
    print(tabela, f"\n\nMedia: {media}\nResultado: {conceito}")

elif 6.0 <= media < 7.5:
    conceito = "C"
    print(tabela, f"\n\nMedia: {media}\nResultado: {conceito}")

elif 4.0 <= media < 6.0:
    conceito = "D"
    print(tabela, f"\n\nMedia: {media}\nResultado: {conceito}")

elif 4.0 > media > 0:
    conceito = "E" 
    print(tabela, f"\n\nMedia: {media}\nResultado: {conceito}")
    
else:
    print("Média invalida")
    


        
        
        