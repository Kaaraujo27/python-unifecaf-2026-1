# Leia 2 listas e retorne quantos valores existem em. ambas a listas
# Dica: nesse caso será necessário um for dentro de outro for

lista1 = [1, 3, 5, 6, 8]
lista2 = [2, 4, 6, 1, 3]

contador = 0

for num1 in lista1:
    for num2 in lista2:
        if num1 == num2:
            contador +=1
            break

print(f'A quantidade de valores em ambas as listas: {contador}')