def calcular_tinta_e_preco(area):
    cobertura_por_litro = 3
    litros_necessarios = area / cobertura_por_litro
    capacidade_lata = 18
    preco_lata = 80.0
    latas_necessarias = litros_necessarios / capacidade_lata
    latas_necessarias = int(latas_necessarias) + (latas_necessarias % 1 > 0)
    preco_total = latas_necessarias * preco_lata
    return latas_necessarias, preco_total

def main():
    area = float(input("Informe o tamanho da área a ser pintada em metros quadrados: "))
    latas, preco = calcular_tinta_e_preco(area)
    print(f"Você precisará de {latas} lata(s) de tinta.")
    print(f"O preço total é R$ {preco:.2f}.")

if __name__ == "__main__":
    main()






