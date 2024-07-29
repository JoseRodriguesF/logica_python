#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#(0 °C × 9/5) + 32 = 32 °F

celcius = float(input("Digite os graus Celcius: "))

fahrenheit = (celcius * 9/5) + 32

print("Em celcius: ", celcius)
print("Em fahrenheit: ", fahrenheit)

