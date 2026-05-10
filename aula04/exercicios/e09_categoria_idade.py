# Exercício 9
# Leia a idade e classifique: criança (<12), adolescente (<18), adulto.

# escreva seu código abaixo

idade = int(input('Digite a idade: '))
if idade < 12:
    print('Criança')
elif idade < 18:
    print('Adolescente')
else: 
    print('Adulto')