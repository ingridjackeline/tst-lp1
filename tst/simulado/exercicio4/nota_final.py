# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a nota necessária para a aprovação do aluno na disciplina 

media_parcial = float(input())

prova_final = (5 - (media_parcial * 0.6)) / 0.4

print(f"{prova_final:.1f}")
