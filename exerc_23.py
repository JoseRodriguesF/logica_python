#Faça um Programa que leia três números e mostre o maior deles.
numero1 = float(input("Digite um numero: "))
numero2= float(input("Digite um numero: "))
numero3= float(input("Digite um numero: "))

if numero2 < numero1 > numero3:
    print(f"O numero {numero1} é o maior dos numeros digitados")
elif numero1 < numero2 > numero3:
    print(f"O numero {numero2} é o maior dos numeros digitados")
else:
     print(f"O numero {numero3} é o maior dos numeros digitados")