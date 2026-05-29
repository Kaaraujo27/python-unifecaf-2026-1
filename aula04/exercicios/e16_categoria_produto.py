# Exercício 16
# Leia o preço e classifique: barato(<50), médio(<100), caro.

# escreva seu código abaixo

categoria = int(input('Qual é o valor do produto? '))
if categoria <=50:
    print('Produto classificado como barato!')
elif categoria <=100:
    print('Produto classificado como mediano!')
else:
    print('Produto classificado como caro!')
    