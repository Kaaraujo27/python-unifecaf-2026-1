# Enquanto o usuário não digitar 0 continue somando todos os números digitados
# n é um número informado pelo usuário
# dicas:
# - estrutura do while: while condição:
# - use input para ler o número n

n = int(input("Digite um número (0 para sair): "))
soma = 0
while n != 0:
    soma += n
    n = int(input("Digite um número (0 para sair): "))
print("A soma de todos os números digitados é:", soma)