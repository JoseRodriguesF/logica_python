#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = input("Qual o preço do produto1? :")
produto2 = input("Qual o preço do produto2? :")
produto3 = input("Qual o preço do produto3? :")

menor = produto1

if produto2 < menor:
    menor = produto2
    print("Você deve comprar o produto 2 pois é o mais barato")
elif produto3 < menor:
    menor = produto3
    print("Você deve comprar o produto 3 pois é o mais barato")
else:
    print("Você deve comprar o produto 1 pois é o mais barato")

