#Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

periodo = str(input("Em qual periodo você estuda:\nM-Matutino\nV-Verspertino\nN-Noturno\n\nDigite: ")).lower()

if periodo == "m":
    print("Bom dia!!!!")
elif periodo == "v":
    print("Boa Tarde!!!!")
elif periodo == "n":
    print("Boa noite!!!!")
else:
    print("Periodo inválido")

    


