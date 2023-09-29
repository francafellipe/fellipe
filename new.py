#media ponderada de 3 provas
peso1 = 1
peso2 = 2

nota1 = float(input(f'Digite a 1 nota: '))
totalnota1 = nota1*peso1

nota2 = float(input(f'Digite a 2 nota: '))

totalnota2 = nota2*peso1

nota3 = float(input(f'Digite a 3 nota: '))

totalnota3 = nota3*peso2

media = (totalnota1 + totalnota2 + totalnota3)/4

print(f'Sua média foi de {media:.0f} e o aluno está ', end= "")

if media >= 60:
    print(f'Aprovado!')

else:
    print(f'Reprovado!')



