# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que recebe uma matriz quadrada e retorna a soma dos elementos da k-ésima moldura

def soma_moldura(m, k):
	soma_elementos = 0
	
	for i in range(len(m)):
		for j in range(len(m[i])):
			if (i == k or i == len(m) - 1 - k) and (j >= k and j <= len(m) - 1 - k):
				soma_elementos += m[i][j]
			elif (j == k or j == len(m) - 1 - k) and (i >= k and i <= len(m) - 1 - k):
				soma_elementos += m[i][j]
				
	return soma_elementos
