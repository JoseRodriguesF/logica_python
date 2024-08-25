#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Se você for Homem digite M, se for mulher digite F: ")).lower()

if sexo == "m":
    print("Você é do sexo masculino")
elif sexo == "f":
    print("Você é do sexo feminino")
else:
    print("sexo invalido")