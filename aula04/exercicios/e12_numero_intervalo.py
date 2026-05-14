# Exercício 12
# Leia um número e informe se está entre 10 e 20.

# escreva seu código abaixo

def numero_intervalo():
    numero_entrada = float(input('Digite um número: '))
    if 10 < numero_entrada < 20:
        print(f'O número {numero_entrada} está entre 10 e 20.')
    else: 
        print(f'O número {numero_entrada} não está entre 10 e 20.')
numero_intervalo()