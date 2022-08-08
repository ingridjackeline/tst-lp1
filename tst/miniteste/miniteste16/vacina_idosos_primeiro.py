# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que altera a lista para priorizar a vacinação dos idosos

def vacina_idosos(lista):
	posicao_idoso = 0
	
	for i in range(len(lista)):
		if lista[i] >= 60:
			for i in range(i, posicao_idoso, -1):
				lista[i], lista[i - 1] = lista[i - 1], lista[i]
			posicao_idoso += 1	
