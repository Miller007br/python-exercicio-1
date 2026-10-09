reais = float(input('quanto voce tem de dinheiro (em R$)?'))
taxa_cambio = 4.99
dolares = reais / taxa_cambio
print(f'com R${reais:.2f}, voce pode comprar U${dolares:.2f}')