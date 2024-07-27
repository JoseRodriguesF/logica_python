#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
nota_N = 0
N_aluno = 1
alunos = 4

for nota in range(alunos):
    nota_N += 1
    nota1 = float(input(f"digite a nota {nota_N} da materia do aluno {N_aluno}: "))
    nota2 = float(input(f"digite a nota {nota_N} da materia do aluno {N_aluno}: "))
    nota3 = float(input(f"digite a nota {nota_N} da materia do aluno {N_aluno}: "))
    nota4 = float(input(f"digite a nota {nota_N} da materia do aluno {N_aluno}: "))
    nota_N = 0
    media = (nota1 + nota2 + nota3 + nota4)/4
    print(f"A média do aluno {N_aluno} é: {media}")
    N_aluno += 1
