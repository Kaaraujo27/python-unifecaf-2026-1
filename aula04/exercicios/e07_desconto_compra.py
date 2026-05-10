# Exercício 7
# Leia o valor de uma compra. Se for maior que 100, aplique 10% de desconto.

# escreva seu código abaixo

valor_compra = float(input("Digite o valor da compra: "))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_com_desconto = valor_compra - desconto
    print(f"O valor da compra com desconto é: R$ {valor_com_desconto:.2f}")
else:
    print(f"O valor da compra é: R$ {valor_compra:.2f} (sem desconto)")