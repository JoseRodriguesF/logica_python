#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
#

peso_maximo = 50
peso_pescado = int(input("Quantos quilos de peixe você pescou?: "))
taxa_por_kg = 4

if peso_pescado > peso_maximo:
    print("Você pescou mais do que o limite de peso permitido em SP")
    multa = taxa_por_kg * (peso_pescado - peso_maximo)
    print(f"Peso maxímo permitido: {peso_maximo}KG\nPeso da pescaria: {peso_pescado}KG\nValor da multa: R${multa}")
else:
    print("Você pescou abaixo do limite, nâo pagará multas.")
