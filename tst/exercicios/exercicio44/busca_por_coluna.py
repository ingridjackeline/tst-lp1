# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que busca um elemento na matriz e retorna uma lista com as suas posições de ocorrência

def busca_todos_por_coluna_em_matriz(m, e):
	lista_ocorrencia = []
	
	for j in range(len(m[0])):
		for i in range(len(m)):
			if m[i][j] == e:
				lista_ocorrencia.append((i,j))
				
	return lista_ocorrencia			
