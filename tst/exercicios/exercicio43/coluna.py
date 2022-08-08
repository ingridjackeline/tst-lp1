# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna uma coluna da matriz como uma lista de valores

def coluna(matriz, i):
	lista_coluna = []
	
	for linha in matriz:
		lista_coluna.append(linha[i])
		
	return lista_coluna	
