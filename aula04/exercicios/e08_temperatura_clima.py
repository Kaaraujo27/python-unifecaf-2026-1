# Exercício 8
# Leia uma temperatura e classifique: frio (<15), ameno (15-25), quente (>25).

# escreva seu código abaixo

temperatura = float(input("Digite a temperatura em graus Celsius: "))
if temperatura < 15:
    print("A temperatura é classificada como: Frio")
elif 15 <= temperatura <= 25:
    print("A temperatura é classificada como: Ameno")
else:
    print("A temperatura é classificada como: Quente")