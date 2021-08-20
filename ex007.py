# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segunda nota: '))

media = (nota_1 + nota_2) / 2

print('-=' * 10)
print(f'Primeira nota: {nota_1}\n'
      f'Segunda nota:  {nota_2}')
print('--' * 10)
print(f'Média:         {media}')

