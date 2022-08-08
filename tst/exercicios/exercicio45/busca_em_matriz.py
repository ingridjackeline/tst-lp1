# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que busca um elemento na matriz e retorna seus índices ou None

def busca_matriz(m, e):
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j] == e:
				return (i,j)
