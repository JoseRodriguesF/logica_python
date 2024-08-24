#Faça um Programa que peça dois números e imprima o maior deles.

numero1 = float(input("Digite um numero: "))
numero2 = float(input("Digite outro numero: "))

if numero1 > numero2:
    print(numero1," é maior que ",numero2)

elif numero2 > numero1: 
    print(numero2,"é maior que numero ",numero1)

else:
    print("os numeros são iguais ")

