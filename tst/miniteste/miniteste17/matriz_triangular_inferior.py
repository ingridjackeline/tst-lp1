# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que modifica uma matriz quadrada tornando-a triangular inferior

def gera_triangular_inferior(M):
	for i in range(len(M)):
		for j in range(len(M[i])):
			if i < j:
				M[j][i] += M[i][j]
				M[i][j] = 0
