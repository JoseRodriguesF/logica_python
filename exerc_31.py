# Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
# Dicas:
# Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
# Triângulo Equilátero: três lados iguais;
# Triângulo Isósceles: quaisquer dois lados iguais;
# Triângulo Escaleno: três lados diferentes;

lado1 = float(input("Qual tamanho do lado 1 do triangulo?:"))
lado2 = float(input("Qual tamanho do lado 2 do triangulo?:"))
lado3 = float(input("Qual tamanho do lado 3 do triangulo?:"))

if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
    print("\nNão é triângulo")
elif lado2 == lado1 == lado3:
    print("\nTriângulo Equilátero")
elif lado1 == lado3 or lado1 == lado2 or lado3 == lado2:
    print("\nTriângulo Isóceles")
elif lado3 != lado1 != lado2:
    print("\nTriângulo Escaleno")





 