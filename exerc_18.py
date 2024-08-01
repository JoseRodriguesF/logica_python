#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input("Qual o tamanho em MB do arquivo que você deseja baixar: "))
velocidade_link = float(input("Qual a velocidade em Mbps do seu link de internet: "))

tamanho_em_mb = arquivo * 8

tempo_segundos = tamanho_em_mb / velocidade_link

tempo_minutos = tempo_segundos / 60

minutos_inteiros = int(tempo_minutos)

decimais = tempo_minutos - minutos_inteiros

if decimais >= 0.6:
    minutos_inteiros += 1
    decimais = 0

print(f"O tempo estimado é de: {minutos_inteiros} Minutos")