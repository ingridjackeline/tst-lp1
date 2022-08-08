# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que identifica qual aluno teve o melhor desempenho

alunos = int(input())

maior_acerto = 0 
melhor_desempenho = -1	
	
for aluno in range(alunos):
	resultado = input()
	acertos = 0
	for caractere in resultado:
		if caractere == ".":
			acertos += 1	
			
	if acertos > maior_acerto:
		maior_acerto = acertos
		melhor_desempenho = aluno + 1 
		
print(melhor_desempenho)		
			
