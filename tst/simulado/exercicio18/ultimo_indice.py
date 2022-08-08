# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna o índice da última ocorrência de num na lista

def ultimo_indice(num, lista):
	indice_ocorrencia = -1
	
	for i in range(len(lista)):
		if lista[i] == num:
			indice_ocorrencia = i
	
	return indice_ocorrencia		
