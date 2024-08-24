#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input("Digite uma letra: "))

vogais = ['a', 'e', 'i', 'o', 'u']

if letra in vogais:
    print("A letra digitada é vogal")
else:
    print("A letra digitada é consoante")

