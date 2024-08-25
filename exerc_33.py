
# Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data_digitada = input("Digite uma data no formato dd/mm/aaaa: ")

try:
    dia, mes, ano = map(int, data_digitada.split('/'))

    ano_bissexto = (ano % 400 == 0) or (ano % 100 != 0 and ano % 4 == 0)
   
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias_no_mes = 31
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        dias_no_mes = 30
    elif mes == 2:
        dias_no_mes = 29 if ano_bissexto else 28
    else:
        dias_no_mes = 0  

    if 1 <= mes <= 12 and 1 <= dia <= dias_no_mes and ano > 0:
        print(f"{dia:02d}/{mes:02d}/{ano} é uma data válida")
    else:
        print("Data inválida")
except ValueError:
    print("Formato de data inválido. Por favor, digite no formato dd/mm/aaaa.")


