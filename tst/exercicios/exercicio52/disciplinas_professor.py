# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna uma tupla com a lista de disciplinas e o número de créditos alocados para o professor

def disciplinas(alocacao, professor):
	lista_disciplinas = []
	num_creditos = 0
	alocada = False
	
	for chave in alocacao:
		for nome in alocacao[chave]:
			if nome == professor:
				if alocada == False:
					lista_disciplinas.append(chave[0])
					alocada = True 
				num_creditos += chave[1]
		
		if alocada == True:
			alocada = False		
				
	return (lista_disciplinas, num_creditos)			
