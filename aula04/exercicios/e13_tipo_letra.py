# Exercício 13
# Leia uma letra e informe se é vogal ou consoante.

# escreva seu código abaixo

letra = input('Digite uma letra: ').lower()
if letra in 'aeiou':
    print(f'A letra {letra} é uma vogal.')
else:
    print(f'A letra {letra} é uma consoante.')