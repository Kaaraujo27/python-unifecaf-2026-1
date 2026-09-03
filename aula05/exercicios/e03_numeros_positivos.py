# Leia uma lista de inteiros e conte quanto são positivos

numeros = [1, -5, 6, 8, 7, -6, -2, -3, -7]
contador_positivos = 0

for numero in numeros:
    if numero >0:
        contador_positivos +=1

print(f"Quantidade de números positivos: {contador_positivos}")