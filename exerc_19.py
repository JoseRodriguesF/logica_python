#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

numero = float(input("Digite um numero: "))

if numero > 0:
    print("O numero é positivo")

elif numero < 0:
    print("O numero é negativo")
    
else:
    print("O numero que você digitou é = 0")