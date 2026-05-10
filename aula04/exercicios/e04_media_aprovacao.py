# Exercício 4
# Leia duas notas e informe se o aluno foi aprovado (>=7) ou reprovado.

# escreva seu código abaixo

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Aluno aprovado.")
else:
    print("Aluno reprovado.")