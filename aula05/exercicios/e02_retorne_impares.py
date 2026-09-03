# Crie um aplicativo que leia uma lista de inteiros 
# e retorne todos os números ímpares

numeros = [1, 2 , 5, 8, 4, 9]
impares = []

for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)

print(f"Números impares {impares}")